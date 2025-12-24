---
layout: default
title: "HuMo: Human-Centric Video Generation via Collaborative Multi-Modal Conditioning"
---

# HuMo: Human-Centric Video Generation via Collaborative Multi-Modal Conditioning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08519" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08519v1</a>
  <a href="https://arxiv.org/pdf/2509.08519.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08519v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08519v1', 'HuMo: Human-Centric Video Generation via Collaborative Multi-Modal Conditioning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liyang Chen, Tianxiang Ma, Jiawei Liu, Bingchuan Li, Zhuowei Chen, Lijie Liu, Xu He, Gen Li, Qian He, Zhiyong Wu

**分类**: cs.CV, cs.MM

**发布日期**: 2025-09-10

**🔗 代码/项目**: [PROJECT_PAGE](https://phantom-video.github.io/HuMo)

---

## 💡 一句话要点

**HuMo：通过协同多模态条件控制实现以人为中心的视频生成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `多模态融合` `以人为中心` `视听同步` `深度学习` `生成模型` `条件生成`

## 📋 核心要点

1. 现有HCVG方法难以有效协调文本、图像和音频等多模态输入，面临训练数据稀缺和子任务协同困难的挑战。
2. HuMo框架通过构建高质量数据集和设计两阶段渐进式训练范式，实现了多模态输入的协同控制。
3. 实验结果表明，HuMo在主体保持和视听同步等子任务中超越了现有方法，实现了统一的多模态HCVG。

## 📝 摘要（中文）

以人为中心的视频生成(HCVG)旨在从多模态输入（包括文本、图像和音频）合成人物视频。现有方法难以有效协调这些异构模态，原因在于两个挑战：配对的三元组条件训练数据稀缺，以及在多模态输入下，主体保持和视听同步等子任务难以协同。本文提出了HuMo，一个用于协同多模态控制的统一HCVG框架。针对第一个挑战，我们构建了一个高质量数据集，包含多样且配对的文本、参考图像和音频。针对第二个挑战，我们提出了一种具有任务特定策略的两阶段渐进式多模态训练范式。对于主体保持任务，为了保持基础模型的提示遵循和视觉生成能力，我们采用了最小侵入式图像注入策略。对于视听同步任务，除了常用的音频交叉注意力层外，我们提出了一种通过预测进行聚焦的策略，隐式地引导模型将音频与面部区域相关联。为了联合学习跨多模态输入的可控性，我们在先前获得的能力的基础上，逐步整合视听同步任务。在推理过程中，为了灵活和细粒度的多模态控制，我们设计了一种时间自适应的无分类器引导策略，动态调整去噪步骤中的引导权重。大量实验结果表明，HuMo在子任务中超越了专门的state-of-the-art方法，为协同多模态条件HCVG建立了一个统一的框架。

## 🔬 方法详解

**问题定义**：现有以人为中心的视频生成方法难以有效融合文本、图像和音频等多模态信息，主要痛点在于缺乏高质量的配对训练数据，以及难以同时保证生成视频的主体一致性和视听同步性。这些问题限制了生成视频的质量和可控性。

**核心思路**：HuMo的核心思路是通过构建高质量的多模态数据集，并采用两阶段渐进式训练范式，逐步提升模型对不同模态信息的理解和融合能力。通过任务特定的策略，分别优化主体保持和视听同步，最终实现协同的多模态控制。

**技术框架**：HuMo框架包含数据构建、模型训练和推理三个主要阶段。首先，构建包含文本、图像和音频配对的高质量数据集。然后，采用两阶段渐进式训练范式，第一阶段侧重于主体保持，第二阶段逐步整合视听同步任务。在推理阶段，使用时间自适应的无分类器引导策略，实现灵活的多模态控制。

**关键创新**：HuMo的关键创新在于：1) 构建了高质量的多模态数据集，为模型训练提供了充足的数据支持；2) 提出了两阶段渐进式训练范式，有效解决了多模态信息融合的难题；3) 提出了最小侵入式图像注入策略和基于预测的聚焦策略，分别优化了主体保持和视听同步效果；4) 设计了时间自适应的无分类器引导策略，实现了灵活的多模态控制。

**关键设计**：在主体保持阶段，采用最小侵入式图像注入策略，避免过度修改基础模型，保持其生成能力。在视听同步阶段，除了音频交叉注意力层外，还引入了基于预测的聚焦策略，通过预测面部区域来引导模型关注音频相关区域。时间自适应的无分类器引导策略根据去噪步骤动态调整引导权重，实现更精细的控制。

## 📊 实验亮点

HuMo在多个实验中均取得了显著的性能提升。例如，在主体保持方面，HuMo能够生成与参考图像高度一致的人物视频。在视听同步方面，HuMo生成的视频能够准确地将音频与人物的面部表情和动作同步。实验结果表明，HuMo在多项指标上超越了现有的state-of-the-art方法，证明了其有效性和优越性。

## 🎯 应用场景

HuMo框架具有广泛的应用前景，例如虚拟形象定制、电影制作、游戏开发、社交媒体内容生成等。该技术可以根据用户的文本描述、参考图像和音频，生成高度逼真且可控的人物视频，极大地提升了内容创作的效率和质量。未来，HuMo有望成为多媒体内容生成领域的重要工具。

## 📄 摘要（原文）

> Human-Centric Video Generation (HCVG) methods seek to synthesize human videos from multimodal inputs, including text, image, and audio. Existing methods struggle to effectively coordinate these heterogeneous modalities due to two challenges: the scarcity of training data with paired triplet conditions and the difficulty of collaborating the sub-tasks of subject preservation and audio-visual sync with multimodal inputs. In this work, we present HuMo, a unified HCVG framework for collaborative multimodal control. For the first challenge, we construct a high-quality dataset with diverse and paired text, reference images, and audio. For the second challenge, we propose a two-stage progressive multimodal training paradigm with task-specific strategies. For the subject preservation task, to maintain the prompt following and visual generation abilities of the foundation model, we adopt the minimal-invasive image injection strategy. For the audio-visual sync task, besides the commonly adopted audio cross-attention layer, we propose a focus-by-predicting strategy that implicitly guides the model to associate audio with facial regions. For joint learning of controllabilities across multimodal inputs, building on previously acquired capabilities, we progressively incorporate the audio-visual sync task. During inference, for flexible and fine-grained multimodal control, we design a time-adaptive Classifier-Free Guidance strategy that dynamically adjusts guidance weights across denoising steps. Extensive experimental results demonstrate that HuMo surpasses specialized state-of-the-art methods in sub-tasks, establishing a unified framework for collaborative multimodal-conditioned HCVG. Project Page: https://phantom-video.github.io/HuMo.

