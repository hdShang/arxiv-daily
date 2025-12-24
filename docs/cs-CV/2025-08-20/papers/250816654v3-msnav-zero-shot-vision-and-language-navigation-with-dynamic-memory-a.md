---
layout: default
title: "MSNav: Zero-Shot Vision-and-Language Navigation with Dynamic Memory and LLM Spatial Reasoning"
---

# MSNav: Zero-Shot Vision-and-Language Navigation with Dynamic Memory and LLM Spatial Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16654" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16654v3</a>
  <a href="https://arxiv.org/pdf/2508.16654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16654v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16654v3', 'MSNav: Zero-Shot Vision-and-Language Navigation with Dynamic Memory and LLM Spatial Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenghao Liu, Zhimu Zhou, Jiachen Zhang, Minghao Zhang, Songfang Huang, Huiling Duan

**分类**: cs.CV

**发布日期**: 2025-08-20 (更新: 2025-09-10)

**备注**: 9 pages, 4 figures

---

## 💡 一句话要点

**提出MSNav框架以解决视觉语言导航中的空间推理与记忆问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `空间推理` `动态记忆` `多模态融合` `大型语言模型`

## 📋 核心要点

1. 现有视觉语言导航方法存在空间推理能力不足和记忆管理不善的问题，导致在复杂环境中的导航效果不佳。
2. 本文提出MSNav框架，通过动态记忆、空间推理和决策模块的协同工作，提升了长时间任务中的导航性能。
3. 在Room-to-Room和REVERIE数据集上的实验结果显示，MSNav在成功率和路径长度加权成功率上均显著优于现有方法。

## 📝 摘要（中文）

视觉语言导航（VLN）要求智能体解读自然语言指令并在复杂环境中导航。现有方法常采用“黑箱”模式，依赖单一的大型语言模型（LLM）进行端到端决策，但存在空间推理不足、跨模态基础薄弱和长时间任务中的记忆过载等关键问题。为系统性解决这些问题，本文提出了记忆空间导航（MSNav）框架，融合了动态记忆模块、空间推理模块和决策模块，增强了推理的稳健性。通过引入指令-对象-空间（I-O-S）数据集，并对Qwen3-4B模型进行微调，MSNav在对象列表提取上超越了领先的商业LLM，实验证明其在Room-to-Room（R2R）和REVERIE数据集上表现出色，成功率和路径长度加权成功率均有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言导航中的空间推理不足和记忆过载问题。现有方法依赖单一LLM进行决策，导致在复杂环境中表现不佳。

**核心思路**：MSNav框架通过整合动态记忆模块、空间推理模块和决策模块，形成一个协同的智能体架构，增强了推理的稳健性和记忆管理能力。

**技术框架**：MSNav的整体架构包括三个主要模块：动态记忆模块负责选择性节点修剪以应对记忆过载，空间推理模块用于空间关系推理和端点识别，决策模块则利用LLM进行路径规划和执行。

**关键创新**：MSNav的核心创新在于其模块化设计，通过动态记忆和空间推理的结合，显著提升了导航的准确性和效率，与传统的黑箱方法形成鲜明对比。

**关键设计**：在技术细节上，MSNav引入了指令-对象-空间（I-O-S）数据集，并对Qwen3-4B模型进行了微调，形成了Qwen-Spatial（Qwen-Sp），在对象列表提取任务中表现优异，F1和NDCG分数均高于现有商业LLM。

## 📊 实验亮点

在Room-to-Room和REVERIE数据集上的实验结果显示，MSNav在成功率（SR）和路径长度加权成功率（SPL）上均显著提升，具体性能数据未提供，但相较于现有方法表现出色，展示了其在视觉语言导航领域的领先地位。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人导航、自动驾驶、虚拟现实和增强现实等场景。通过提升视觉语言导航的能力，MSNav能够在复杂环境中更好地理解和执行人类指令，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) requires an agent to interpret natural language instructions and navigate complex environments. Current approaches often adopt a "black-box" paradigm, where a single Large Language Model (LLM) makes end-to-end decisions. However, it is plagued by critical vulnerabilities, including poor spatial reasoning, weak cross-modal grounding, and memory overload in long-horizon tasks. To systematically address these issues, we propose Memory Spatial Navigation(MSNav), a framework that fuses three modules into a synergistic architecture, which transforms fragile inference into a robust, integrated intelligence. MSNav integrates three modules: Memory Module, a dynamic map memory module that tackles memory overload through selective node pruning, enhancing long-range exploration; Spatial Module, a module for spatial reasoning and object relationship inference that improves endpoint recognition; and Decision Module, a module using LLM-based path planning to execute robust actions. Powering Spatial Module, we also introduce an Instruction-Object-Space (I-O-S) dataset and fine-tune the Qwen3-4B model into Qwen-Spatial (Qwen-Sp), which outperforms leading commercial LLMs in object list extraction, achieving higher F1 and NDCG scores on the I-O-S test set. Extensive experiments on the Room-to-Room (R2R) and REVERIE datasets demonstrate MSNav's state-of-the-art performance with significant improvements in Success Rate (SR) and Success weighted by Path Length (SPL).

