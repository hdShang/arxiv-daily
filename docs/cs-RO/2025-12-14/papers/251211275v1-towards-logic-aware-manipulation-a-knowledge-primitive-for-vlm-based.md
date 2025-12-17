---
layout: default
title: Towards Logic-Aware Manipulation: A Knowledge Primitive for VLM-Based Assistants in Smart Manufacturing
---

# Towards Logic-Aware Manipulation: A Knowledge Primitive for VLM-Based Assistants in Smart Manufacturing

**arXiv**: [2512.11275v1](https://arxiv.org/abs/2512.11275) | [PDF](https://arxiv.org/pdf/2512.11275.pdf)

**作者**: Suchang Chen, Daqiang Guo

---

## 💡 一句话要点

**提出面向智能制造的物体中心操作逻辑模式，以增强视觉语言模型在机器人操作中的执行参数感知能力。**

**关键词**: `视觉语言模型` `机器人操作` `智能制造` `知识原语` `逻辑感知规划` `数据增强`

## 📋 核心要点

1. 现有视觉语言模型在机器人操作中缺乏执行关键参数，如力和轨迹，影响制造场景下的接触丰富动作。
2. 定义八字段元组τ作为知识原语，显式编码物体、接口、轨迹、容差和力/阻抗信息，连接操作员、助手和控制器。
3. 在3D打印机线轴移除任务中实例化τ和知识库，评估τ条件下的规划质量，并展示其在训练数据增强和测试时逻辑感知提示中的应用。

## 📄 摘要（原文）

> Existing pipelines for vision-language models (VLMs) in robotic manipulation prioritize broad semantic generalization from images and language, but typically omit execution-critical parameters required for contact-rich actions in manufacturing cells. We formalize an object-centric manipulation-logic schema, serialized as an eight-field tuple τ, which exposes object, interface, trajectory, tolerance, and force/impedance information as a first-class knowledge signal between human operators, VLM-based assistants, and robot controllers. We instantiate τ and a small knowledge base (KB) on a 3D-printer spool-removal task in a collaborative cell, and analyze τ-conditioned VLM planning using plan-quality metrics adapted from recent VLM/LLM planning benchmarks, while demonstrating how the same schema supports taxonomy-tagged data augmentation at training time and logic-aware retrieval-augmented prompting at test time as a building block for assistant systems in smart manufacturing enterprises.

