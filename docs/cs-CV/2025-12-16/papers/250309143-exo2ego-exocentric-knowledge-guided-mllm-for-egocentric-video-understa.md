---
layout: default
title: Exo2Ego: Exocentric Knowledge Guided MLLM for Egocentric Video Understanding
---

# Exo2Ego: Exocentric Knowledge Guided MLLM for Egocentric Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2503.09143" class="toolbar-btn" target="_blank">📄 arXiv: 2503.09143</a>
  <a href="https://arxiv.org/pdf/2503.09143.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2503.09143" onclick="toggleFavorite(this, '2503.09143', 'Exo2Ego: Exocentric Knowledge Guided MLLM for Egocentric Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Zhang, Qiaohui Chu, Meng Liu, Haoxiang Shi, Yaowei Wang, Liqiang Nie

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Exo2Ego，利用外视知识指导MLLM进行第一人称视频理解**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内视视频理解` `多模态大语言模型` `知识迁移` `外视知识` `具身智能`

## 📋 核心要点

1. 现有MLLM主要关注外视视觉，忽略了内视视频理解的特殊性，且内视数据获取成本高昂。
2. 提出学习外视到内视的知识迁移，利用外视MLLM的知识增强内视视频理解能力。
3. 构建Ego-ExoClip和EgoIT数据集，并设计渐进式映射学习流程，实验表明模型性能显著提升。

## 📝 摘要（中文）

为了使AI助手能够更好地与人类协作，需要具备具身理解能力。然而，目前的多模态大语言模型(MLLMs)主要关注第三人称(外视)视觉，忽略了第一人称(内视)视频的独特挑战。此外，高昂的数据采集成本限制了数据规模，影响了MLLM的性能。为了解决这些问题，我们提出学习外视和内视域之间的映射，利用现有MLLM中丰富的外视知识来增强内视视频理解。为此，我们引入了Ego-ExoClip，一个包含110万个同步内视-外视剪辑-文本对的预训练数据集，该数据集源自Ego-Exo4D。同时，我们收集了来自多个来源的指令调优数据集EgoIT，以增强模型的指令遵循能力。基于这些数据集，我们提出了一种迁移策略，并进一步设计了一个包含三个阶段的渐进式映射学习流程：演示者自我准备、演示者-学习者指导和学习者自我实践。在各种内视任务上的大量实验表明，现有的MLLM在内视视频理解方面表现不足，而我们的模型显著优于这些领先模型。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型(MLLMs)在第一人称(内视)视频理解方面的不足。现有MLLMs主要针对第三人称(外视)视觉进行训练，缺乏对内视视频中视角、动作和交互的理解能力。此外，内视视频数据采集成本高，导致数据规模有限，进一步限制了MLLMs的性能。

**核心思路**：论文的核心思路是利用现有的、经过大量外视数据训练的MLLMs所具备的丰富知识，通过学习外视和内视域之间的映射，将外视知识迁移到内视视频理解任务中。这种方法旨在克服内视数据稀缺的问题，并充分利用现有MLLMs的强大能力。

**技术框架**：整体框架包含三个主要阶段：
1. **演示者自我准备(Demonstrator Self-Preparation)**：利用外视数据预训练MLLM，使其具备基本的外视知识。
2. **演示者-学习者指导(Demonstrator-Learner Guidance)**：利用Ego-ExoClip数据集，通过对比学习等方法，训练模型学习外视和内视之间的对应关系，将外视知识迁移到内视域。
3. **学习者自我实践(Learner Self-Practice)**：利用EgoIT数据集，通过指令调优，进一步提升模型在内视视频理解任务中的性能和指令遵循能力。

**关键创新**：论文的关键创新在于提出了一种基于知识迁移的内视视频理解方法，通过学习外视和内视域之间的映射，有效地利用了现有MLLMs的知识。此外，Ego-ExoClip数据集的构建也为内视视频理解研究提供了新的资源。与现有方法相比，该方法无需从头训练MLLM，而是通过知识迁移的方式，更高效地提升了内视视频理解的性能。

**关键设计**：
1. **Ego-ExoClip数据集**：包含110万个同步内视-外视剪辑-文本对，用于学习外视和内视之间的对应关系。
2. **EgoIT数据集**：包含多个来源的指令数据，用于指令调优，提升模型性能。
3. **渐进式映射学习流程**：包含演示者自我准备、演示者-学习者指导和学习者自我实践三个阶段，逐步提升模型在内视视频理解任务中的性能。
4. **迁移策略**：具体迁移策略细节未知，但应包含如何将外视知识有效迁移到内视域的方法。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.09143/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.09143/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.09143/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有的MLLM在内视视频理解方面表现不佳，而提出的Exo2Ego模型显著优于这些领先模型。具体的性能数据和提升幅度未知，但摘要强调了“显著优于”的结果，表明该方法在内视视频理解方面取得了重要进展。

## 🎯 应用场景

该研究成果可应用于开发更智能的AI个人助手，例如部署在机器人或可穿戴设备上的助手，能够更好地理解用户的意图和行为，从而提供更有效的帮助和支持。此外，该技术还可应用于智能家居、智能安防、医疗健康等领域，提升相关系统的智能化水平。

## 📄 摘要（原文）

> AI personal assistants, deployed through robots or wearables, require embodied understanding to collaborate effectively with humans. However, current Multimodal Large Language Models (MLLMs) primarily focus on third-person (exocentric) vision, overlooking the unique challenges of first-person (egocentric) videos. Additionally, high acquisition costs limit data size, impairing MLLM performance. To address these challenges, we propose learning the mapping between exocentric and egocentric domains, leveraging the extensive exocentric knowledge within existing MLLMs to enhance egocentric video understanding. To this end, we introduce Ego-ExoClip, a pre-training dataset comprising 1.1M synchronized ego-exo clip-text pairs derived from Ego-Exo4D, together with the instruction-tuning dataset EgoIT, which is collected from multiple sources to enhance the model's instruction-following capabilities. Building upon the datasets, we propose a migration strategy and further design a progressive mapping learning pipeline with three stages: Demonstrator Self-Preparation, Demonstrator-Learner Guidance, and Learner Self-Practice. Extensive experiments across diverse egocentric tasks reveal that existing MLLMs perform inadequately in egocentric video understanding, while our model significantly outperforms these leading models.

