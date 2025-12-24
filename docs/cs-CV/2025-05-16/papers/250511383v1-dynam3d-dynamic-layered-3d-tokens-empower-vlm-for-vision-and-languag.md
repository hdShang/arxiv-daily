---
layout: default
title: Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation
---

# Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11383" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11383v1</a>
  <a href="https://arxiv.org/pdf/2505.11383.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11383v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11383v1', 'Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Seungjun Lee, Gim Hee Lee

**分类**: cs.CV, cs.RO

**发布日期**: 2025-05-16

---

## 💡 一句话要点

**提出Dynam3D以解决3D导航中的动态环境适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉与语言导航` `动态环境适应` `3D表示` `长时间记忆` `机器人导航` `多模态学习` `空间语义理解`

## 📋 核心要点

1. 现有视频语言大模型在3D导航中面临3D几何理解不足和动态环境适应差等挑战。
2. Dynam3D通过动态分层3D表示，结合语言对齐的特征，提升了3D几何和语义理解能力。
3. 在R2R-CE、REVERIE-CE和NavRAG-CE等基准测试中，Dynam3D实现了新的性能记录，验证了其实用性。

## 📝 摘要（中文）

视觉与语言导航（VLN）是一个核心任务，涉及智能体根据自然语言指令在3D环境中导航。尽管视频语言大模型（Video-VLMs）在VLN任务中表现出色，但仍面临3D几何理解不足、环境记忆有限及动态环境适应差等挑战。为此，本文提出Dynam3D，一个动态分层3D表示模型，通过语言对齐的层次化3D表示来训练3D-VLM进行导航动作预测。Dynam3D能够在线编码和定位3D实例，并在变化的环境中动态更新，从而实现大规模探索和长期记忆能力。实验结果表明，Dynam3D在多个VLN基准测试中设定了新的最先进性能，并验证了其在实际部署中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频语言大模型在3D导航任务中对3D几何和空间语义理解不足、环境记忆能力有限及动态环境适应性差的问题。

**核心思路**：Dynam3D通过构建动态分层3D表示，利用语言对齐的特征来增强3D-VLM的导航动作预测能力，旨在实现更好的环境理解和适应性。

**技术框架**：Dynam3D的整体架构包括多个模块：首先，输入RGB-D图像，接着将2D CLIP特征投影到3D空间，构建多层次的3D补丁-实例-区域表示，最后通过动态更新策略实现在线编码和定位。

**关键创新**：Dynam3D的核心创新在于其动态分层表示方法，能够在变化环境中实时更新3D实例，与传统方法相比，显著提升了对动态环境的适应能力。

**关键设计**：在设计上，Dynam3D采用了层次化的特征表示和动态更新策略，确保了对大规模环境的探索和长期记忆能力，同时在损失函数和网络结构上进行了优化，以适应导航任务的需求。

## 📊 实验亮点

在多个视觉与语言导航基准测试中，Dynam3D实现了新的最先进性能，具体在R2R-CE、REVERIE-CE和NavRAG-CE测试中，相较于现有基线模型，性能提升幅度显著，验证了其在实际应用中的有效性和可靠性。

## 🎯 应用场景

Dynam3D的研究成果在多个领域具有潜在应用价值，包括机器人导航、增强现实和虚拟现实等。通过提升智能体在动态环境中的导航能力，该技术能够为实际应用提供更高的灵活性和适应性，推动智能体在复杂环境中的部署与应用。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) is a core task where embodied agents leverage their spatial mobility to navigate in 3D environments toward designated destinations based on natural language instructions. Recently, video-language large models (Video-VLMs) with strong generalization capabilities and rich commonsense knowledge have shown remarkable performance when applied to VLN tasks. However, these models still encounter the following challenges when applied to real-world 3D navigation: 1) Insufficient understanding of 3D geometry and spatial semantics; 2) Limited capacity for large-scale exploration and long-term environmental memory; 3) Poor adaptability to dynamic and changing environments.To address these limitations, we propose Dynam3D, a dynamic layered 3D representation model that leverages language-aligned, generalizable, and hierarchical 3D representations as visual input to train 3D-VLM in navigation action prediction. Given posed RGB-D images, our Dynam3D projects 2D CLIP features into 3D space and constructs multi-level 3D patch-instance-zone representations for 3D geometric and semantic understanding with a dynamic and layer-wise update strategy. Our Dynam3D is capable of online encoding and localization of 3D instances, and dynamically updates them in changing environments to provide large-scale exploration and long-term memory capabilities for navigation. By leveraging large-scale 3D-language pretraining and task-specific adaptation, our Dynam3D sets new state-of-the-art performance on VLN benchmarks including R2R-CE, REVERIE-CE and NavRAG-CE under monocular settings. Furthermore, experiments for pre-exploration, lifelong memory, and real-world robot validate the effectiveness of practical deployment.

