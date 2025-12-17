---
layout: default
title: ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications
---

# ROSBag MCP Server: Analyzing Robot Data with LLMs for Agentic Embodied AI Applications

**arXiv**: [2511.03497v1](https://arxiv.org/abs/2511.03497) | [PDF](https://arxiv.org/pdf/2511.03497.pdf)

**作者**: Lei Fu, Sahar Salimpour, Leonardo Militano, Harry Edelman, Jorge Peña Queralta, Giovanni Toffetti

---

## 💡 一句话要点

**提出ROS包MCP服务器，使LLM能分析机器人数据以支持具身AI应用。**

**关键词**: `具身AI` `模型上下文协议` `ROS数据分析` `自然语言处理` `机器人视觉` `代理系统`

## 📋 核心要点

1. 核心问题：具身AI与代理AI交叉领域研究稀缺，缺乏自然语言分析机器人数据的工具。
2. 方法要点：构建MCP服务器，集成ROS包分析工具，支持轨迹、激光扫描等数据处理。
3. 实验或效果：评估八种LLM/VLM工具调用能力，Kimi K2和Claude Sonnet 4表现最佳。

## 📄 摘要（原文）

> Agentic AI systems and Physical or Embodied AI systems have been two key
> research verticals at the forefront of Artificial Intelligence and Robotics,
> with Model Context Protocol (MCP) increasingly becoming a key component and
> enabler of agentic applications. However, the literature at the intersection of
> these verticals, i.e., Agentic Embodied AI, remains scarce. This paper
> introduces an MCP server for analyzing ROS and ROS 2 bags, allowing for
> analyzing, visualizing and processing robot data with natural language through
> LLMs and VLMs. We describe specific tooling built with robotics domain
> knowledge, with our initial release focused on mobile robotics and supporting
> natively the analysis of trajectories, laser scan data, transforms, or time
> series data. This is in addition to providing an interface to standard ROS 2
> CLI tools ("ros2 bag list" or "ros2 bag info"), as well as the ability to
> filter bags with a subset of topics or trimmed in time. Coupled with the MCP
> server, we provide a lightweight UI that allows the benchmarking of the tooling
> with different LLMs, both proprietary (Anthropic, OpenAI) and open-source
> (through Groq). Our experimental results include the analysis of tool calling
> capabilities of eight different state-of-the-art LLM/VLM models, both
> proprietary and open-source, large and small. Our experiments indicate that
> there is a large divide in tool calling capabilities, with Kimi K2 and Claude
> Sonnet 4 demonstrating clearly superior performance. We also conclude that
> there are multiple factors affecting the success rates, from the tool
> description schema to the number of arguments, as well as the number of tools
> available to the models. The code is available with a permissive license at
> https://github.com/binabik-ai/mcp-rosbags.

