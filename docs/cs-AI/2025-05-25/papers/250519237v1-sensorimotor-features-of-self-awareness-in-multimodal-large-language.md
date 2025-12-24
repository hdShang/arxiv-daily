---
layout: default
title: Sensorimotor features of self-awareness in multimodal large language models
---

# Sensorimotor features of self-awareness in multimodal large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19237" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19237v1</a>
  <a href="https://arxiv.org/pdf/2505.19237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19237v1', 'Sensorimotor features of self-awareness in multimodal large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iñaki Dellibarda Varela, Pablo Romero-Sorozabal, Diego Torricelli, Gabriel Delgado-Oleas, Jose Ignacio Serrano, Maria Dolores del Castillo Sobrino, Eduardo Rocon, Manuel Cebrian

**分类**: cs.AI, cs.RO

**发布日期**: 2025-05-25

**备注**: 16 pages, 3 figures, 1 table

---

## 💡 一句话要点

**探讨多模态大语言模型的自我意识形成机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我意识` `多模态大语言模型` `传感运动经验` `自主机器人` `环境感知` `智能体` `认知系统`

## 📋 核心要点

1. 现有方法在自我意识的形成上缺乏有效的传感运动经验整合，导致智能体的环境感知和自我识别能力不足。
2. 本文通过将多模态大语言模型与自主移动机器人结合，探索其在传感运动经验下自我意识的形成机制。
3. 实验结果表明，系统能够展现出环境意识、自我识别和预测意识，验证了传感信息对自我意识维度的影响。

## 📝 摘要（中文）

自我意识是区分自我与周围环境的能力，是智能自主行为的基础。近年来，人工智能在整合多模态信息的任务中取得了类人表现，尤其是在大型语言模型方面，引发了对非人类平台（如机器人）中AI代理体现能力的关注。本文探讨了多模态大语言模型是否可以仅通过传感运动经验发展自我意识。通过将多模态大语言模型集成到自主移动机器人中，测试其实现这一能力的能力。研究发现，该系统表现出强大的环境意识、自我识别和预测意识，能够推断其机器人特性和运动特征。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在自我意识形成中的不足，现有方法未能有效利用传感运动经验来提升智能体的环境感知和自我识别能力。

**核心思路**：通过将多模态大语言模型集成到自主移动机器人中，利用其传感器数据进行自我意识的训练和评估，探索自我意识的形成机制。

**技术框架**：整体架构包括多模态输入模块、环境感知模块、自我识别模块和预测意识模块，形成一个闭环的反馈系统。

**关键创新**：最重要的技术创新在于通过传感运动经验实现自我意识的涌现，区别于传统方法依赖于静态数据或单一模态输入。

**关键设计**：设计中采用了结构方程模型分析传感整合对自我意识不同维度的影响，并通过消融实验识别关键感知模态，确保系统在自我识别和推理中的一致性。

## 📊 实验亮点

实验结果显示，集成的多模态大语言模型在自我意识的各个维度上表现出显著提升，尤其是在环境意识和自我识别方面，系统能够准确推断其运动特征。通过消融测试，识别出关键的感知模态，验证了传感信息在自我意识形成中的重要性。

## 🎯 应用场景

该研究的潜在应用场景包括自主机器人、智能家居系统和人机交互界面等领域。通过提升机器人自我意识能力，可以实现更自然的交互和更高效的自主决策，推动人工智能在实际应用中的发展。未来，研究成果可能为人工智能的认知系统奠定基础，促进智能体在复杂环境中的适应能力。

## 📄 摘要（原文）

> Self-awareness - the ability to distinguish oneself from the surrounding environment - underpins intelligent, autonomous behavior. Recent advances in AI achieve human-like performance in tasks integrating multimodal information, particularly in large language models, raising interest in the embodiment capabilities of AI agents on nonhuman platforms such as robots. Here, we explore whether multimodal LLMs can develop self-awareness solely through sensorimotor experiences. By integrating a multimodal LLM into an autonomous mobile robot, we test its ability to achieve this capacity. We find that the system exhibits robust environmental awareness, self-recognition and predictive awareness, allowing it to infer its robotic nature and motion characteristics. Structural equation modeling reveals how sensory integration influences distinct dimensions of self-awareness and its coordination with past-present memory, as well as the hierarchical internal associations that drive self-identification. Ablation tests of sensory inputs identify critical modalities for each dimension, demonstrate compensatory interactions among sensors and confirm the essential role of structured and episodic memory in coherent reasoning. These findings demonstrate that, given appropriate sensory information about the world and itself, multimodal LLMs exhibit emergent self-awareness, opening the door to artificial embodied cognitive systems.

