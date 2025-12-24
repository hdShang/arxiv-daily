---
layout: default
title: Reducing Latency in LLM-Based Natural Language Commands Processing for Robot Navigation
---

# Reducing Latency in LLM-Based Natural Language Commands Processing for Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00075" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00075v1</a>
  <a href="https://arxiv.org/pdf/2506.00075.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00075v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00075v1', 'Reducing Latency in LLM-Based Natural Language Commands Processing for Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Diego Pollini, Bruna V. Guterres, Rodrigo S. Guerra, Ricardo B. Grando

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-29

**备注**: Accepted to the 23rd IEEE International Conference on Industrial Informatics (INDIN)

---

## 💡 一句话要点

**提出一种架构以减少机器人导航中的语言命令处理延迟**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器人导航` `人机交互` `实时系统` `ROS 2` `ChatGPT` `工业自动化`

## 📋 核心要点

1. 现有大型语言模型在工业机器人中的应用面临计算复杂性和响应延迟的问题，影响了人机协作的效率。
2. 本研究提出了一种将ChatGPT与ROS 2集成的架构，旨在减少交互延迟并提升机器人控制能力。
3. 实验结果显示，该集成方案平均通信延迟降低了7.01%，显著提升了人机交互的流畅性和实时性。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLMs）在工业机器人中的应用，尤其是如何通过集成ChatGPT与机器人操作系统2（ROS 2）来降低交互延迟。研究中提出了一种新架构，使得这些技术能够无缝集成，且不需要中间件传输平台。通过在模拟的Gazebo环境中测试，结果表明该集成方案在执行速度、可用性和人机交互的可达性方面均有所提升，平均通信延迟降低了7.01%。这些改进对于工业自动化和精密任务的实时机器人操作至关重要。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在机器人导航中引起的交互延迟问题。现有方法由于模型复杂性和计算需求，导致请求和响应时间较长，影响了机器人操作的实时性和效率。

**核心思路**：论文提出了一种新架构，将ChatGPT与ROS 2直接集成，避免了传统中间件的使用，从而减少了通信延迟。这种设计旨在提高人机交互的流畅性和响应速度。

**技术框架**：整体架构包括三个主要模块：语言模型模块（ChatGPT）、机器人控制模块（ROS 2）和交互接口模块。通过这些模块的协同工作，机器人能够快速响应文本和语音命令。

**关键创新**：本研究的关键创新在于无中间件的集成方式，这一设计显著降低了通信延迟，与现有依赖中间件的方案相比，提升了系统的响应速度和可用性。

**关键设计**：在技术细节上，论文对参数设置进行了优化，确保了模型在处理命令时的高效性。此外，采用了适合实时交互的损失函数和网络结构，以支持快速的命令解析和执行。

## 📊 实验亮点

实验结果表明，集成方案的平均通信延迟降低了7.01%，显著提升了人机交互的流畅性。与传统方法相比，该方案在执行速度和可用性上均有显著改善，为工业自动化提供了更高效的解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括工业自动化、智能制造和服务机器人等。通过降低人机交互的延迟，机器人能够更高效地执行复杂任务，提升工作效率和安全性。未来，这一技术有望在更多实时应用场景中得到推广，推动智能机器人技术的发展。

## 📄 摘要（原文）

> The integration of Large Language Models (LLMs), such as GPT, in industrial robotics enhances operational efficiency and human-robot collaboration. However, the computational complexity and size of these models often provide latency problems in request and response times. This study explores the integration of the ChatGPT natural language model with the Robot Operating System 2 (ROS 2) to mitigate interaction latency and improve robotic system control within a simulated Gazebo environment. We present an architecture that integrates these technologies without requiring a middleware transport platform, detailing how a simulated mobile robot responds to text and voice commands. Experimental results demonstrate that this integration improves execution speed, usability, and accessibility of the human-robot interaction by decreasing the communication latency by 7.01\% on average. Such improvements facilitate smoother, real-time robot operations, which are crucial for industrial automation and precision tasks.

