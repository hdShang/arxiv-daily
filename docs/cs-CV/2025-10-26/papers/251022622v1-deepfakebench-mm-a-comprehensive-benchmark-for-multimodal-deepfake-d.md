---
layout: default
title: DeepfakeBench-MM: A Comprehensive Benchmark for Multimodal Deepfake Detection
---

# DeepfakeBench-MM: A Comprehensive Benchmark for Multimodal Deepfake Detection

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22622" target="_blank" class="toolbar-btn">arXiv: 2510.22622v1</a>
    <a href="https://arxiv.org/pdf/2510.22622.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22622v1" 
            onclick="toggleFavorite(this, '2510.22622v1', 'DeepfakeBench-MM: A Comprehensive Benchmark for Multimodal Deepfake Detection')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kangran Zhao, Yupeng Chen, Xiaoyu Zhang, Yize Chen, Weinan Guan, Baicheng Chen, Chengzhe Sun, Soumyya Kanti Datta, Qingshan Liu, Siwei Lyu, Baoyuan Wu

**分类**: cs.CR, cs.CV, cs.MM

**发布日期**: 2025-10-26

**备注**: Preprint

---

## 💡 一句话要点

**构建多模态深度伪造检测基准，应对伪造音视频内容带来的社会风险。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度伪造检测` `多模态学习` `数据集构建` `基准测试` `音频伪造` `视频伪造` `人工智能安全` `对抗样本`

## 📋 核心要点

1. 现有深度伪造检测缺乏足够多样的数据集和标准化的评估基准，阻碍了更深入的研究。
2. 构建大规模多模态数据集Mega-MMDF，并提出统一的评估基准DeepfakeBench-MM，促进深度伪造检测研究。
3. 通过综合评估，揭示了数据增强和堆叠伪造等因素对检测性能的影响，为未来研究提供指导。

## 📝 摘要（中文）

针对生成式AI模型滥用导致的虚假数据泛滥问题，特别是伪造的人类音视频内容带来的社会风险，本文构建了大规模、多样化、高质量的多模态深度伪造检测数据集Mega-MMDF。该数据集包含0.1百万真实样本和1.1百万伪造样本，通过组合10种音频伪造方法、12种视觉伪造方法和6种音频驱动的面部重演方法，共计21种伪造流程生成。同时，提出了首个统一的多模态深度伪造检测基准DeepfakeBench-MM，建立了标准化的检测流程，为评估现有方法和探索新方法提供平台。通过全面的评估和深入的分析，揭示了多个关键发现，例如数据增强和堆叠伪造的影响。DeepfakeBench-MM和Mega-MMDF将为推进多模态深度伪造检测提供基础。

## 🔬 方法详解

**问题定义**：论文旨在解决日益猖獗的多模态深度伪造内容检测问题。现有的深度伪造检测方法受限于数据集规模和多样性不足，缺乏统一的评估标准，难以有效应对复杂场景下的伪造内容，并且难以进行公平的性能比较。

**核心思路**：论文的核心思路是构建一个大规模、多样化的多模态深度伪造数据集Mega-MMDF，并在此基础上建立一个统一的评估基准DeepfakeBench-MM。通过提供充足的训练数据和标准化的评估流程，促进多模态深度伪造检测技术的发展。

**技术框架**：DeepfakeBench-MM的整体框架包含数据集构建、模型评估和结果分析三个主要阶段。数据集构建阶段，通过组合多种音频和视频伪造技术，生成大规模的Mega-MMDF数据集。模型评估阶段，在DeepfakeBench-MM上对现有和新的多模态深度伪造检测模型进行评估。结果分析阶段，对评估结果进行深入分析，揭示不同因素对检测性能的影响。

**关键创新**：论文的关键创新在于构建了大规模、多样化的多模态深度伪造数据集Mega-MMDF，并提出了首个统一的多模态深度伪造检测基准DeepfakeBench-MM。Mega-MMDF数据集的规模和多样性远超现有数据集，DeepfakeBench-MM基准的标准化评估流程为公平比较不同方法提供了可能。

**关键设计**：Mega-MMDF数据集通过组合10种音频伪造方法、12种视觉伪造方法和6种音频驱动的面部重演方法，共计21种伪造流程生成。DeepfakeBench-MM基准定义了标准化的数据预处理、模型训练和评估流程，并提供了多种评估指标，例如准确率、精确率、召回率和F1值。

## 📊 实验亮点

论文构建的Mega-MMDF数据集包含1.1百万伪造样本，规模远超现有数据集。DeepfakeBench-MM基准支持11种多模态深度伪造检测器，并进行了全面的评估和分析，揭示了数据增强和堆叠伪造等因素对检测性能的影响。实验结果表明，现有方法在Mega-MMDF数据集上的性能仍有提升空间。

## 🎯 应用场景

该研究成果可应用于金融安全、社会舆情监控、新闻真实性验证等领域，有效防范深度伪造技术带来的欺诈、诽谤等风险，维护社会稳定和信息安全。未来可进一步扩展到更多模态数据，提升检测模型的鲁棒性和泛化能力。

## 📄 摘要（原文）

> The misuse of advanced generative AI models has resulted in the widespread proliferation of falsified data, particularly forged human-centric audiovisual content, which poses substantial societal risks (e.g., financial fraud and social instability). In response to this growing threat, several works have preliminarily explored countermeasures. However, the lack of sufficient and diverse training data, along with the absence of a standardized benchmark, hinder deeper exploration. To address this challenge, we first build Mega-MMDF, a large-scale, diverse, and high-quality dataset for multimodal deepfake detection. Specifically, we employ 21 forgery pipelines through the combination of 10 audio forgery methods, 12 visual forgery methods, and 6 audio-driven face reenactment methods. Mega-MMDF currently contains 0.1 million real samples and 1.1 million forged samples, making it one of the largest and most diverse multimodal deepfake datasets, with plans for continuous expansion. Building on it, we present DeepfakeBench-MM, the first unified benchmark for multimodal deepfake detection. It establishes standardized protocols across the entire detection pipeline and serves as a versatile platform for evaluating existing methods as well as exploring novel approaches. DeepfakeBench-MM currently supports 5 datasets and 11 multimodal deepfake detectors. Furthermore, our comprehensive evaluations and in-depth analyses uncover several key findings from multiple perspectives (e.g., augmentation, stacked forgery). We believe that DeepfakeBench-MM, together with our large-scale Mega-MMDF, will serve as foundational infrastructures for advancing multimodal deepfake detection.

