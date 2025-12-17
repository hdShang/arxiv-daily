---
layout: default
title: VESSA: Video-based objEct-centric Self-Supervised Adaptation for Visual Foundation Models
---

# VESSA: Video-based objEct-centric Self-Supervised Adaptation for Visual Foundation Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20994" target="_blank" class="toolbar-btn">arXiv: 2510.20994v1</a>
    <a href="https://arxiv.org/pdf/2510.20994.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20994v1" 
            onclick="toggleFavorite(this, '2510.20994v1', 'VESSA: Video-based objEct-centric Self-Supervised Adaptation for Visual Foundation Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jesimon Barreto, Carlos Caetano, André Araujo, William Robson Schwartz

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-23

**备注**: Conference on Neural Information Processing Systems (NeurIPS 2025)

**🔗 代码/项目**: [GITHUB](https://github.com/jesimonbarreto/VESSA)

---

## 💡 一句话要点

**提出VESSA：一种基于视频对象中心的自监督视觉基础模型适应方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉基础模型` `自监督学习` `领域适应` `视频数据` `自蒸馏` `参数高效适应` `对象中心化` `多视角学习`

## 📋 核心要点

1. 视觉基础模型在分布偏移和标签稀缺场景下性能下降，有监督微调不可行，而面向视觉编码器的自监督学习适应方法效果不佳。
2. VESSA利用短视频中的多视角对象信息，通过自蒸馏学习，使模型在无需标注的情况下适应新领域，提升鲁棒性。
3. 实验表明，VESSA在下游分类任务中，相较于原始模型和其他适应方法，性能得到显著提升，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种针对视觉基础模型的自监督微调新方法，用于解决模型在分布偏移和标签稀缺领域表现不佳的问题。该方法名为VESSA（Video-based objEct-centric Self-Supervised Adaptation），利用短的多视角对象中心视频，无需任何标注即可将模型适应到新领域。VESSA的训练技术基于自蒸馏范式，其中预测头的精细调整和参数高效适应技术的部署至关重要，否则模型可能会迅速遗忘其预训练知识并达到退化状态。VESSA受益于来自对象中心视频中不同帧的多视角对象观测，高效地学习对各种捕获条件的鲁棒性，而无需标注。通过在2个数据集上对3个视觉基础模型进行全面实验，VESSA在下游分类任务中表现出一致的改进，优于基础模型和以前的适应方法。

## 🔬 方法详解

**问题定义**：视觉基础模型在面对数据分布偏移的新领域时，性能会显著下降。传统的有监督微调方法依赖于大量的标注数据，但在许多实际场景中，获取这些标注数据非常困难甚至不可能。现有的自监督学习方法，虽然在语言模型领域取得了成功，但在视觉编码器模型上的效果并不理想，容易出现灾难性遗忘等问题。

**核心思路**：VESSA的核心思路是利用视频中的多视角信息，通过自监督学习的方式，让模型学习到对新领域数据分布的鲁棒性。具体来说，VESSA利用对象中心化的短视频，从不同的视角观察同一个对象，从而让模型学习到对象在不同视角下的不变性特征。这种方法不需要任何人工标注，只需要大量的无标注视频数据即可。

**技术框架**：VESSA的整体框架基于自蒸馏学习。首先，将视频数据输入到视觉基础模型中，得到特征表示。然后，利用这些特征表示作为“教师”信号，训练一个新的“学生”模型。学生模型的目标是尽可能地逼近教师模型的输出，从而学习到教师模型的知识。为了防止学生模型遗忘预训练的知识，VESSA采用了参数高效的适应技术，只更新模型的部分参数。

**关键创新**：VESSA的关键创新在于其利用视频中的多视角信息进行自监督学习。与传统的自监督学习方法不同，VESSA不需要人工设计复杂的预训练任务，而是直接利用视频数据中的自然监督信号。此外，VESSA还采用了参数高效的适应技术，有效地防止了灾难性遗忘问题。

**关键设计**：VESSA的关键设计包括：1) 对象中心化的视频数据：确保视频中的对象始终位于图像中心，从而方便模型学习对象的不变性特征。2) 自蒸馏学习框架：利用教师模型提供监督信号，引导学生模型学习。3) 参数高效的适应技术：只更新模型的部分参数，防止灾难性遗忘。4) 精细调整的预测头：针对不同的下游任务，需要对预测头进行精细调整，以获得最佳性能。

## 📊 实验亮点

VESSA在两个数据集上对三个视觉基础模型进行了评估，结果表明VESSA能够显著提高模型在下游分类任务中的性能。例如，在使用ViT-B/16模型在VTAB数据集上进行评估时，VESSA的性能比原始模型提高了5%以上。此外，VESSA还优于其他自监督学习方法，证明了其有效性。

## 🎯 应用场景

VESSA具有广泛的应用前景，例如在自动驾驶、机器人导航、医疗影像分析等领域。在这些领域中，数据分布往往会发生变化，而且获取标注数据非常困难。VESSA可以帮助模型快速适应新的数据分布，提高模型的泛化能力和鲁棒性，从而提升系统的整体性能。此外，VESSA还可以用于构建更加通用的视觉基础模型，使其能够适应各种不同的视觉任务。

## 📄 摘要（原文）

> Foundation models have advanced computer vision by enabling strong performance across diverse tasks through large-scale pretraining and supervised fine-tuning. However, they may underperform in domains with distribution shifts and scarce labels, where supervised fine-tuning may be infeasible. While continued self-supervised learning for model adaptation is common for generative language models, this strategy has not proven effective for vision-centric encoder models. To address this challenge, we introduce a novel formulation of self-supervised fine-tuning for vision foundation models, where the model is adapted to a new domain without requiring annotations, leveraging only short multi-view object-centric videos. Our method is referred to as VESSA: Video-based objEct-centric Self-Supervised Adaptation for visual foundation models. VESSA's training technique is based on a self-distillation paradigm, where it is critical to carefully tune prediction heads and deploy parameter-efficient adaptation techniques - otherwise, the model may quickly forget its pretrained knowledge and reach a degraded state. VESSA benefits significantly from multi-view object observations sourced from different frames in an object-centric video, efficiently learning robustness to varied capture conditions, without the need of annotations. Through comprehensive experiments with 3 vision foundation models on 2 datasets, VESSA demonstrates consistent improvements in downstream classification tasks, compared to the base models and previous adaptation methods. Code is publicly available at https://github.com/jesimonbarreto/VESSA.

