---
layout: default
title: A Large Language Model Based Pipeline for Review of Systems Entity Recognition from Clinical Notes
---

# A Large Language Model Based Pipeline for Review of Systems Entity Recognition from Clinical Notes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11067" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11067v1</a>
  <a href="https://arxiv.org/pdf/2506.11067.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11067v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11067v1', 'A Large Language Model Based Pipeline for Review of Systems Entity Recognition from Clinical Notes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hieu Nghiem, Hemanth Reddy Singareddy, Zhuqi Miao, Jivan Lamichhane, Abdulaziz Ahmed, Johnson Thomas, Dursun Delen, William Paiva

**分类**: cs.CL

**发布日期**: 2025-05-31

---

## 💡 一句话要点

**提出基于大语言模型的管道以自动提取临床笔记中的系统回顾实体**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `系统回顾` `临床笔记` `实体识别` `开源技术` `自动化提取` `医疗记录`

## 📋 核心要点

1. 现有方法在临床笔记中提取系统回顾实体时，面临高成本和低效率的问题。
2. 论文提出了一种基于大语言模型的管道，利用开源LLM和少量示例技术来自动化提取ROS实体。
3. 实验结果表明，集成ChatGPT的管道在实体检测和状态识别上实现了显著的错误率降低。

## 📝 摘要（中文）

本研究旨在开发一种经济高效的基于大语言模型（LLM）的管道，自动提取临床笔记中的系统回顾（ROS）实体。该管道首先使用SecTag提取ROS部分，然后通过少量示例的LLM识别ROS实体范围、其正负状态及相关身体系统。我们使用开源LLM（如Mistral、Llama、Gemma）和ChatGPT实现了该管道，并在36份包含341个标注ROS实体的一般医学笔记上进行了评估。结果显示，集成ChatGPT后，该管道在检测ROS实体范围及其状态/系统方面的错误率最低（分别为28.2%和14.5%）。开源LLM使得该管道能够在本地以低成本执行，同时在错误率方面表现出色（范围：30.5-36.7%；状态/系统：24.3-27.3%）。

## 🔬 方法详解

**问题定义**：本研究旨在解决在临床笔记中自动提取系统回顾（ROS）实体的挑战。现有方法通常成本高且效率低，难以满足医疗环境的需求。

**核心思路**：论文的核心思路是利用大语言模型（LLM）和少量示例技术，构建一个自动化管道，以提高ROS实体提取的准确性和效率。通过开源LLM的使用，降低了实施成本。

**技术框架**：该管道的整体架构包括两个主要模块：首先使用SecTag提取ROS部分，然后通过少量示例的LLM识别ROS实体的范围、状态及相关身体系统。

**关键创新**：本研究的关键创新在于结合了开源LLM与少量示例技术，提供了一种可扩展且经济高效的解决方案，能够在资源有限的医疗环境中替代商业模型。

**关键设计**：在设计中，使用了多种开源LLM（如Mistral、Llama、Gemma）和ChatGPT，评估了不同模型在实体检测中的表现，设置了相应的参数以优化识别精度。实验中采用了341个标注的ROS实体进行验证。

## 📊 实验亮点

实验结果显示，集成ChatGPT的管道在检测ROS实体范围时的错误率为28.2%，状态识别的错误率为14.5%。开源LLM的表现也相当出色，错误率范围为30.5-36.7%（范围）和24.3-27.3%（状态/系统），展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗记录自动化、临床决策支持系统以及电子健康记录的智能化处理。通过减少医生的文书工作负担，提升临床效率，未来可能对医疗服务的质量和可及性产生积极影响。

## 📄 摘要（原文）

> Objective: Develop a cost-effective, large language model (LLM)-based pipeline for automatically extracting Review of Systems (ROS) entities from clinical notes. Materials and Methods: The pipeline extracts ROS sections using SecTag, followed by few-shot LLMs to identify ROS entity spans, their positive/negative status, and associated body systems. We implemented the pipeline using open-source LLMs (Mistral, Llama, Gemma) and ChatGPT. The evaluation was conducted on 36 general medicine notes containing 341 annotated ROS entities. Results: When integrating ChatGPT, the pipeline achieved the lowest error rates in detecting ROS entity spans and their corresponding statuses/systems (28.2% and 14.5%, respectively). Open-source LLMs enable local, cost-efficient execution of the pipeline while delivering promising performance with similarly low error rates (span: 30.5-36.7%; status/system: 24.3-27.3%). Discussion and Conclusion: Our pipeline offers a scalable and locally deployable solution to reduce ROS documentation burden. Open-source LLMs present a viable alternative to commercial models in resource-limited healthcare environments.

