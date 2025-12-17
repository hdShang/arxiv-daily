---
layout: default
title: The Quest for Generalizable Motion Generation: Data, Model, and Evaluation
---

# The Quest for Generalizable Motion Generation: Data, Model, and Evaluation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.26794" target="_blank" class="toolbar-btn">arXiv: 2510.26794v1</a>
    <a href="https://arxiv.org/pdf/2510.26794.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26794v1" 
            onclick="toggleFavorite(this, '2510.26794v1', 'The Quest for Generalizable Motion Generation: Data, Model, and Evaluation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jing Lin, Ruisi Wang, Junzhe Lu, Ziqi Huang, Guorui Song, Ailing Zeng, Xian Liu, Chen Wei, Wanqi Yin, Qingping Sun, Zhongang Cai, Lei Yang, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-10-30

---

## 💡 一句话要点

**提出ViMoGen框架，通过迁移视频生成知识，提升3D人体动作生成模型的泛化能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D人体动作生成` `视频生成` `知识迁移` `扩散模型` `多模态融合`

## 📋 核心要点

1. 现有3D人体动作生成模型在泛化能力上存在瓶颈，难以适应复杂多样的场景。
2. ViMoGen框架通过数据增强、模型设计和评估体系三个方面，将视频生成领域的知识迁移到动作生成领域。
3. 实验结果表明，ViMoGen在动作质量、提示保真度和泛化能力上均优于现有方法，具有显著优势。

## 📝 摘要（中文）

本文针对现有3D人体动作生成(MoGen)模型泛化能力不足的问题，提出了一种综合框架，系统地将视频生成(ViGen)领域的知识迁移到MoGen领域，涵盖数据、建模和评估三个关键方面。首先，构建了一个大规模数据集ViMoGen-228K，包含22.8万个高质量动作样本，集成了高保真光学MoCap数据、来自网络视频的语义标注动作以及ViGen模型合成的样本，显著扩展了语义多样性。其次，提出了ViMoGen，一个基于流匹配的扩散Transformer，通过门控多模态条件作用统一了MoCap数据和ViGen模型的先验知识。为了提高效率，进一步开发了ViMoGen-light，一个精简版本，消除了对视频生成的依赖，同时保留了强大的泛化能力。最后，提出了MBench，一个分层基准，用于对运动质量、提示保真度和泛化能力进行细粒度评估。大量实验表明，该框架在自动和人工评估中均显著优于现有方法。代码、数据和基准将公开。

## 🔬 方法详解

**问题定义**：现有3D人体动作生成模型在标准数据集上表现良好，但在实际应用中泛化能力不足，难以生成自然、符合语义的动作。现有方法通常依赖于有限的MoCap数据，缺乏对复杂场景和语义信息的有效建模。

**核心思路**：借鉴视频生成领域的成功经验，将视频生成模型中学习到的先验知识迁移到动作生成任务中。通过融合MoCap数据和视频数据，增强模型的语义理解能力和泛化能力。

**技术框架**：ViMoGen框架包含三个主要组成部分：大规模数据集ViMoGen-228K、基于流匹配的扩散Transformer模型ViMoGen和分层评估基准MBench。ViMoGen-228K数据集融合了MoCap数据、视频数据和合成数据，为模型训练提供丰富的样本。ViMoGen模型通过门控多模态条件作用，将文本、视频和MoCap数据融合在一起，生成高质量的动作序列。MBench基准用于全面评估模型的性能。

**关键创新**：该论文的关键创新在于将视频生成领域的知识迁移到动作生成领域，并提出了相应的框架和模型。通过融合多模态数据，增强了模型的语义理解能力和泛化能力。此外，还提出了一个分层评估基准，用于全面评估模型的性能。

**关键设计**：ViMoGen模型采用基于流匹配的扩散Transformer架构，通过门控机制融合多模态信息。损失函数包括流匹配损失、运动学损失和对抗损失等。ViMoGen-light模型通过知识蒸馏，将ViMoGen模型的知识迁移到更轻量级的模型中，提高了推理效率。

## 📊 实验亮点

ViMoGen在MBench基准测试中取得了显著的性能提升。在动作质量方面，ViMoGen优于现有方法。在提示保真度方面，ViMoGen能够更好地生成符合文本描述的动作。在泛化能力方面，ViMoGen在未见过的场景和动作上表现出更强的鲁棒性。人工评估也表明，ViMoGen生成的动作更加自然和逼真。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏开发、动画制作、机器人控制等领域。例如，可以根据用户的文本描述或视频输入，生成逼真的人体动作，从而增强用户体验。此外，该技术还可以用于训练机器人，使其能够更好地理解人类的意图并执行相应的动作。

## 📄 摘要（原文）

> Despite recent advances in 3D human motion generation (MoGen) on standard benchmarks, existing models still face a fundamental bottleneck in their generalization capability. In contrast, adjacent generative fields, most notably video generation (ViGen), have demonstrated remarkable generalization in modeling human behaviors, highlighting transferable insights that MoGen can leverage. Motivated by this observation, we present a comprehensive framework that systematically transfers knowledge from ViGen to MoGen across three key pillars: data, modeling, and evaluation. First, we introduce ViMoGen-228K, a large-scale dataset comprising 228,000 high-quality motion samples that integrates high-fidelity optical MoCap data with semantically annotated motions from web videos and synthesized samples generated by state-of-the-art ViGen models. The dataset includes both text-motion pairs and text-video-motion triplets, substantially expanding semantic diversity. Second, we propose ViMoGen, a flow-matching-based diffusion transformer that unifies priors from MoCap data and ViGen models through gated multimodal conditioning. To enhance efficiency, we further develop ViMoGen-light, a distilled variant that eliminates video generation dependencies while preserving strong generalization. Finally, we present MBench, a hierarchical benchmark designed for fine-grained evaluation across motion quality, prompt fidelity, and generalization ability. Extensive experiments show that our framework significantly outperforms existing approaches in both automatic and human evaluations. The code, data, and benchmark will be made publicly available.

