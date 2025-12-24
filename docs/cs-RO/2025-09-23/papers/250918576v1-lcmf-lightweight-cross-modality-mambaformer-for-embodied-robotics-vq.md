---
layout: default
title: "LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA"
---

# LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18576" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18576v1</a>
  <a href="https://arxiv.org/pdf/2509.18576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18576v1', 'LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyi Kang, Liang He, Yanxin Zhang, Zuheng Ming, Kaixing Zhao

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-23

---

## 💡 一句话要点

**提出轻量级跨模态Mambaformer（LCMF），用于具身机器人VQA任务。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身机器人` `视觉问答` `多模态融合` `Mamba架构` `跨模态注意力` `参数共享` `轻量化模型`

## 📋 核心要点

1. 现有方法难以有效融合异构数据，且在资源受限环境下计算效率低，限制了具身智能的发展。
2. 提出LCMF框架，通过多层跨模态参数共享机制的Mamba模块，实现异构模态高效融合和语义对齐。
3. 实验表明，LCMF在VQA任务中准确率达74.29%，FLOPs比基线平均水平降低4.35倍。

## 📝 摘要（中文）

本研究针对具身智能中多模态语义学习面临的异构数据融合和资源受限环境下的计算效率问题，提出了轻量级LCMF级联注意力框架。该框架将多层跨模态参数共享机制引入Mamba模块，结合Cross-Attention和选择性参数共享状态空间模型（SSM）的优势，实现了异构模态的高效融合和语义互补对齐。实验结果表明，LCMF在VQA任务中超越了现有的多模态基线，准确率达到74.29%，并在EQA视频任务中达到了大型语言模型代理（LLM Agents）分布集群中具有竞争力的中等水平性能。其轻量化设计实现了相对于可比基线平均水平4.35倍的FLOPs减少，同时仅使用166.51M（图像-文本）和219M（视频-文本）参数，为资源受限场景下的人机交互（HRI）应用提供了高效的解决方案，并具有强大的多模态决策泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决具身机器人视觉问答（VQA）任务中，如何高效融合多模态信息（如图像、文本、视频），并在计算资源有限的机器人平台上实现高性能的问题。现有方法通常计算量大，难以部署在资源受限的机器人上，且多模态信息融合效率不高。

**核心思路**：论文的核心思路是将Mamba架构与跨模态注意力机制相结合，并引入多层参数共享策略，从而在保证性能的同时，显著降低模型的计算复杂度。Mamba架构擅长序列建模，跨模态注意力则能有效融合不同模态的信息。参数共享进一步减少了模型参数量。

**技术框架**：LCMF框架主要包含以下几个模块：首先，使用预训练模型（如视觉Transformer和文本编码器）提取图像、文本或视频的特征。然后，将这些特征输入到LCMF模块中进行跨模态融合。LCMF模块的核心是Mamba模块，其中集成了跨模态注意力机制和多层参数共享策略。最后，通过一个预测头输出答案。

**关键创新**：论文最重要的技术创新点在于将Mamba架构与跨模态注意力机制相结合，并提出了多层参数共享策略。Mamba架构擅长序列建模，能够有效处理多模态信息之间的依赖关系。跨模态注意力机制则能够自适应地融合不同模态的信息。多层参数共享策略则显著降低了模型的参数量，使其更适合部署在资源受限的机器人平台上。

**关键设计**：LCMF框架的关键设计包括：1) 使用选择性参数共享状态空间模型（SSM），在不同模态之间共享部分参数，减少模型参数量；2) 采用Cross-Attention机制，实现不同模态特征之间的有效交互；3) 通过级联多个LCMF模块，逐步提升模型的表达能力；4) 损失函数采用标准的交叉熵损失函数，用于训练VQA模型。

## 📊 实验亮点

实验结果表明，LCMF在VQA任务中取得了74.29%的准确率，超越了现有的多模态基线。同时，LCMF的FLOPs相对于可比基线平均水平降低了4.35倍，参数量仅为166.51M（图像-文本）和219M（视频-文本）。此外，LCMF在EQA视频任务中也达到了大型语言模型代理（LLM Agents）分布集群中具有竞争力的中等水平性能，验证了其强大的多模态决策泛化能力。

## 🎯 应用场景

该研究成果可应用于多种人机交互场景，例如家庭服务机器人、工业巡检机器人、医疗辅助机器人等。通过高效的多模态信息融合和决策能力，机器人可以更好地理解人类指令，感知周围环境，并做出智能决策，从而提升人机交互的效率和安全性。未来，该技术有望推动具身智能在更多领域的应用。

## 📄 摘要（原文）

> Multimodal semantic learning plays a critical role in embodied intelligence, especially when robots perceive their surroundings, understand human instructions, and make intelligent decisions. However, the field faces technical challenges such as effective fusion of heterogeneous data and computational efficiency in resource-constrained environments. To address these challenges, this study proposes the lightweight LCMF cascaded attention framework, introducing a multi-level cross-modal parameter sharing mechanism into the Mamba module. By integrating the advantages of Cross-Attention and Selective parameter-sharing State Space Models (SSMs), the framework achieves efficient fusion of heterogeneous modalities and semantic complementary alignment. Experimental results show that LCMF surpasses existing multimodal baselines with an accuracy of 74.29% in VQA tasks and achieves competitive mid-tier performance within the distribution cluster of Large Language Model Agents (LLM Agents) in EQA video tasks. Its lightweight design achieves a 4.35-fold reduction in FLOPs relative to the average of comparable baselines while using only 166.51M parameters (image-text) and 219M parameters (video-text), providing an efficient solution for Human-Robot Interaction (HRI) applications in resource-constrained scenarios with strong multimodal decision generalization capabilities.

