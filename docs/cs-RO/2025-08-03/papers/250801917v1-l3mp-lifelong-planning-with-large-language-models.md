---
layout: default
title: "L3M+P: Lifelong Planning with Large Language Models"
---

# L3M+P: Lifelong Planning with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01917" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01917v1</a>
  <a href="https://arxiv.org/pdf/2508.01917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01917v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01917v1', 'L3M+P: Lifelong Planning with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Krish Agarwal, Yuqian Jiang, Jiaheng Hu, Bo Liu, Peter Stone

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出L3M+P框架以解决服务机器人长期规划问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长期规划` `大型语言模型` `知识图谱` `服务机器人` `动态记忆` `自然语言处理` `经典规划`

## 📋 核心要点

1. 现有的规划方法在服务机器人长期部署中面临环境规范不一致和动态记忆维护的挑战。
2. L3M+P框架通过外部知识图谱来表示和更新环境状态，支持多模态输入和自然语言交互。
3. 在家庭机器人模拟器和真实服务机器人上评估，L3M+P在自然语言状态变化注册和规划生成上显著优于基线方法。

## 📝 摘要（中文）

通过结合经典规划方法与大型语言模型（LLMs），L3M+P框架旨在解决服务机器人在动态环境中进行长期规划的挑战。现有方法通常需要详细且一致的环境规范，而L3M+P通过外部知识图谱来表示世界状态，支持从多种信息源更新图谱。该框架在规划时利用自然语言任务描述，从知识图谱中检索上下文并生成问题定义，显著提高了自然语言状态变化的注册准确性和规划生成的正确性。

## 🔬 方法详解

**问题定义**：本论文旨在解决服务机器人在动态环境中进行长期规划时，现有方法对环境规范要求过高且缺乏动态记忆维护的问题。

**核心思路**：L3M+P框架通过引入外部知识图谱，允许机器人从多种信息源更新环境状态，并在规划时利用这些信息生成任务定义。

**技术框架**：L3M+P的整体架构包括知识图谱的构建与更新模块、自然语言处理模块和经典规划模块。知识图谱通过传感器输入和人机交互不断更新，确保信息的一致性和准确性。

**关键创新**：L3M+P的主要创新在于使用知识图谱作为世界状态的表示，解决了传统方法在动态环境中难以维护一致性的缺陷。

**关键设计**：框架中设计了规则以确保知识图谱的更新格式一致性，此外，规划时通过检索知识图谱中的上下文信息来生成问题定义，提升了规划的准确性和效率。

## 📊 实验亮点

在实验中，L3M+P在家庭机器人模拟器和真实服务机器人上表现出色，准确注册自然语言状态变化的能力显著提高，规划生成的正确性也得到了显著提升。与基线方法相比，L3M+P在这两个方面的性能均有显著改善，具体提升幅度未知。

## 🎯 应用场景

L3M+P框架具有广泛的应用潜力，特别是在家庭服务机器人、智能助理和其他需要长期交互的机器人系统中。通过动态更新环境状态，机器人能够更好地理解和适应用户需求，从而提供更个性化的服务。未来，该框架还可扩展到更多复杂的任务和环境中，提升机器人自主决策能力。

## 📄 摘要（原文）

> By combining classical planning methods with large language models (LLMs), recent research such as LLM+P has enabled agents to plan for general tasks given in natural language. However, scaling these methods to general-purpose service robots remains challenging: (1) classical planning algorithms generally require a detailed and consistent specification of the environment, which is not always readily available; and (2) existing frameworks mainly focus on isolated planning tasks, whereas robots are often meant to serve in long-term continuous deployments, and therefore must maintain a dynamic memory of the environment which can be updated with multi-modal inputs and extracted as planning knowledge for future tasks. To address these two issues, this paper introduces L3M+P (Lifelong LLM+P), a framework that uses an external knowledge graph as a representation of the world state. The graph can be updated from multiple sources of information, including sensory input and natural language interactions with humans. L3M+P enforces rules for the expected format of the absolute world state graph to maintain consistency between graph updates. At planning time, given a natural language description of a task, L3M+P retrieves context from the knowledge graph and generates a problem definition for classical planners. Evaluated on household robot simulators and on a real-world service robot, L3M+P achieves significant improvement over baseline methods both on accurately registering natural language state changes and on correctly generating plans, thanks to the knowledge graph retrieval and verification.

