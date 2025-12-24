---
layout: default
title: "PeftCD: Leveraging Vision Foundation Models with Parameter-Efficient Fine-Tuning for Remote Sensing Change Detection"
---

# PeftCD: Leveraging Vision Foundation Models with Parameter-Efficient Fine-Tuning for Remote Sensing Change Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09572" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09572v1</a>
  <a href="https://arxiv.org/pdf/2509.09572.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09572v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09572v1', 'PeftCD: Leveraging Vision Foundation Models with Parameter-Efficient Fine-Tuning for Remote Sensing Change Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sijun Dong, Yuxuan Hu, LiBo Wang, Geng Chen, Xiaoliang Meng

**分类**: cs.CV

**发布日期**: 2025-09-11

**🔗 代码/项目**: [GITHUB](https://github.com/dyzy41/PeftCD)

---

## 💡 一句话要点

**PeftCD：利用参数高效微调的视觉基础模型进行遥感变化检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感变化检测` `视觉基础模型` `参数高效微调` `Siamese网络` `LoRA` `Adapter` `伪变化抑制`

## 📋 核心要点

1. 遥感变化检测面临伪变化干扰、标注数据不足和跨领域泛化性差等挑战。
2. PeftCD利用视觉基础模型，通过参数高效微调，实现快速适应特定遥感变化检测任务。
3. 实验表明，PeftCD在多个数据集上达到SOTA，有效抑制伪变化，边界划分更精确。

## 📝 摘要（中文）

为了解决多时相和多源遥感图像中伪变化普遍、标记样本稀缺以及跨域泛化困难的问题，我们提出了PeftCD，这是一个建立在视觉基础模型（VFMs）之上，并采用参数高效微调（PEFT）的变化检测框架。PeftCD的核心是采用一个源自VFM的权重共享Siamese编码器，其中无缝集成了LoRA和Adapter模块。这种设计通过仅训练最少数量的附加参数来实现高效的任务适应。为了充分释放VFM的潜力，我们研究了两个领先的骨干网络：以强大的分割先验而闻名的Segment Anything Model v2（SAM2）和最先进的自监督表示学习器DINOv3。该框架由一个精心设计的轻量级解码器补充，确保重点仍然放在来自骨干网络的强大特征表示上。大量实验表明，PeftCD在多个公共数据集上实现了最先进的性能，包括SYSU-CD（IoU 73.81%）、WHUCD（92.05%）、MSRSCD（64.07%）、MLCD（76.89%）、CDD（97.01%）、S2Looking（52.25%）和LEVIR-CD（85.62%），具有显著精确的边界描绘和对伪变化的强大抑制。总之，PeftCD在准确性、效率和泛化性之间实现了最佳平衡。它为将大规模VFM应用于实际遥感变化检测应用提供了一个强大且可扩展的范例。

## 🔬 方法详解

**问题定义**：遥感变化检测旨在识别不同时间获取的同一区域遥感图像之间的差异。现有方法通常需要大量标注数据进行训练，且容易受到伪变化的影响，泛化能力有限。此外，直接微调大型视觉模型成本高昂，效率低下。

**核心思路**：PeftCD的核心在于利用预训练的视觉基础模型（VFMs）的强大特征提取能力，并通过参数高效微调（PEFT）方法，仅训练少量参数即可适应特定的变化检测任务。这种方法既能利用VFM的通用知识，又能避免从头训练或全参数微调带来的高成本和过拟合风险。

**技术框架**：PeftCD采用Siamese网络结构，包含两个共享权重的编码器，分别处理不同时相的遥感图像。编码器基于VFM（如SAM2或DINOv3），并集成LoRA或Adapter模块进行参数高效微调。编码器提取的特征经过轻量级解码器进行融合和处理，最终输出变化检测结果。整体流程包括：图像输入 -> VFM编码器（LoRA/Adapter微调） -> 特征提取 -> 轻量级解码器 -> 变化检测结果。

**关键创新**：PeftCD的关键创新在于将参数高效微调技术与视觉基础模型相结合，用于遥感变化检测。通过LoRA或Adapter等PEFT方法，仅需训练少量参数即可实现对VFM的有效适应，显著降低了计算成本和存储需求，同时保持了较高的检测精度。此外，该方法对伪变化的抑制能力更强，泛化性能更好。

**关键设计**：PeftCD的关键设计包括：1) 选择合适的VFM作为骨干网络，如SAM2或DINOv3，利用其强大的特征提取能力；2) 集成LoRA或Adapter模块，实现参数高效微调；3) 设计轻量级解码器，避免引入过多参数，保持模型的简洁性；4) 采用合适的损失函数，如交叉熵损失或Dice损失，优化变化检测结果。

## 📊 实验亮点

PeftCD在多个公开遥感变化检测数据集上取得了SOTA性能，例如在SYSU-CD上IoU达到73.81%，在WHUCD上达到92.05%，在CDD上达到97.01%。相较于传统方法，PeftCD在精度、效率和泛化性方面均有显著提升，尤其在抑制伪变化和精确边界描绘方面表现突出。

## 🎯 应用场景

PeftCD可广泛应用于城市规划、灾害监测、环境评估、农业管理等领域。通过快速准确地检测地表变化，为决策者提供及时有效的信息支持，具有重要的实际应用价值和社会经济效益。未来可进一步扩展到更多类型的遥感数据和更复杂的场景，例如三维变化检测和多模态数据融合。

## 📄 摘要（原文）

> To tackle the prevalence of pseudo changes, the scarcity of labeled samples, and the difficulty of cross-domain generalization in multi-temporal and multi-source remote sensing imagery, we propose PeftCD, a change detection framework built upon Vision Foundation Models (VFMs) with Parameter-Efficient Fine-Tuning (PEFT). At its core, PeftCD employs a weight-sharing Siamese encoder derived from a VFM, into which LoRA and Adapter modules are seamlessly integrated. This design enables highly efficient task adaptation by training only a minimal set of additional parameters. To fully unlock the potential of VFMs, we investigate two leading backbones: the Segment Anything Model v2 (SAM2), renowned for its strong segmentation priors, and DINOv3, a state-of-the-art self-supervised representation learner. The framework is complemented by a deliberately lightweight decoder, ensuring the focus remains on the powerful feature representations from the backbones. Extensive experiments demonstrate that PeftCD achieves state-of-the-art performance across multiple public datasets, including SYSU-CD (IoU 73.81%), WHUCD (92.05%), MSRSCD (64.07%), MLCD (76.89%), CDD (97.01%), S2Looking (52.25%) and LEVIR-CD (85.62%), with notably precise boundary delineation and strong suppression of pseudo-changes. In summary, PeftCD presents an optimal balance of accuracy, efficiency, and generalization. It offers a powerful and scalable paradigm for adapting large-scale VFMs to real-world remote sensing change detection applications. The code and pretrained models will be released at https://github.com/dyzy41/PeftCD.

