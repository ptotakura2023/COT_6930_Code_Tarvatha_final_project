##
## OwlMind - Platform for Education and Experimentation with Generative Intelligent Systems
## bot-1.py :: Agentic Discord Bot using LangChain
## 
#  
# Copyright (c) 2024 The Generative Intelligence Lab @ FAU
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# Documentation and Getting Started:
#    https://github.com/genilab-fau/owlmind
#
# Class Documentation at:
#    https://github.com/genilab-fau/owlmind/bot-1.md
#
# Disclaimer: 
# Generative AI has been used extensively while developing this package.
# 

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import re
from agents import AgentOrchestrator

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

# Load environment variables
load_dotenv()

# Get Discord token from environment
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
if not DISCORD_TOKEN:
    print("Error: DISCORD_TOKEN not found in environment variables.")
    print("Please set the DISCORD_TOKEN in your .env file.")
    exit(1)

# Initialize the bot with command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize the agent orchestrator
orchestrator = AgentOrchestrator()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds:')
    for guild in bot.guilds:
        print(f'- {guild.name} (id: {guild.id})')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Log all messages (for debugging)
    logger.info(f'Message from {message.author}: {message.content}')
    
    # Check if the message is a direct mention of the bot
    if f'<@{bot.user.id}>' in message.content:
        # Extract the question from the mention
        question = message.content.replace(f'<@{bot.user.id}>', '').strip()
        if question:
            # Process the question as if it was a command
            ctx = await bot.get_context(message)
            await ask(ctx, question=question)
            return
    
    # Process commands
    await bot.process_commands(message)

async def process_question(ctx, question):
    """Process a question and send the response"""
    try:
        logger.info(f'Processing question from {ctx.author}: {question}')
        
        # Show that we're analyzing the question
        await ctx.send("🔍 Analyzing your question...")
        
        # Get the classification
        category = orchestrator.classifier.classify(question)
        logger.info(f'Question classified as: {category}')
        
        # Define agent roles and reasons
        agent_roles = {
            "DOUBT_SOLVER": "Doubt Solver Agent",
            "CODE_REVIEW": "Code Review Agent",
            "STUDY_PLANNER": "Study Planner Agent"
        }
        
        classification_reasons = {
            "DOUBT_SOLVER": "This question appears to be about understanding concepts or seeking explanations.",
            "CODE_REVIEW": "This question seems to be related to programming, code, or technical implementation.",
            "STUDY_PLANNER": "This question appears to be about learning strategies or study planning."
        }
        
        # Create and send the agent assignment message
        agent_role = agent_roles.get(category, "Unknown Agent")
        reason = classification_reasons.get(category, "The question could not be clearly categorized.")
        
        assignment_msg = f"""
🤖 **Question Assigned To:** {agent_role}
📝 **Reason:** {reason}
"""
        await ctx.send(assignment_msg)
        
        # Show that we're processing
        await ctx.send("💭 Processing response...")
        
        # Get and send the response
        response = orchestrator.get_response(question)
        logger.info(f'Generated response length: {len(response)} characters')
        
        # Split long responses into chunks if needed
        if len(response) > 1900:  # Discord message limit is 2000
            chunks = [response[i:i+1900] for i in range(0, len(response), 1900)]
            for i, chunk in enumerate(chunks, 1):
                await ctx.send(f"Part {i}/{len(chunks)}:\n{chunk}")
        else:
            await ctx.send(response)
            
    except Exception as e:
        logger.error(f'Error processing question: {str(e)}', exc_info=True)
        await ctx.send(f"❌ Sorry, I encountered an error: {str(e)}")

@bot.command(name='ask')
async def ask(ctx, *, question):
    """Ask a question to the OwlMind bot"""
    await process_question(ctx, question)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ Please provide a question after the !ask command.")
    else:
        logger.error(f'Command error: {str(error)}', exc_info=True)
        await ctx.send(f"❌ An error occurred: {str(error)}")

if __name__ == '__main__':
    # Run the bot with the token from environment variables
    bot.run(DISCORD_TOKEN)

