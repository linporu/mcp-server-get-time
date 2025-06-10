# MCP Get Time Server

A simple [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that provides current local time information to AI assistants and other MCP-compatible clients.

## Features

- 🕐 **Local Time**: Returns current time in user's local timezone
- 🌍 **Timezone Aware**: Automatically detects and includes timezone information
- 📅 **ISO Format**: Returns time in ISO 8601 format for easy parsing
- 🚀 **FastMCP**: Built with FastMCP for simple, Pythonic development
- 🔧 **Easy Integration**: Works with Claude Desktop, Cursor, and other MCP clients

## What it does

This MCP server exposes a single tool called `get_time` that returns the current date and time in the user's local timezone. The time is returned in ISO 8601 format (e.g., `2025-05-23T17:59:21.542827+08:00`), making it perfect for AI assistants to understand and present naturally to users.

## Prerequisites

- Python 3.12
