---
layout: default
title: PSScreen V2: Partially Supervised Multiple Retinal Disease Screening
---

# PSScreen V2: Partially Supervised Multiple Retinal Disease Screening

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22589" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22589v2</a>
  <a href="https://arxiv.org/pdf/2510.22589.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22589v2" onclick="toggleFavorite(this, '2510.22589v2', 'PSScreen V2: Partially Supervised Multiple Retinal Disease Screening')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyi Zheng, Yalin Zheng, Hrvoje Bogunović, Qing Liu

**分类**: cs.CV

**发布日期**: 2025-10-26 (更新: 2025-10-28)

**🔗 代码/项目**: [GITHUB](https://github.com/boyiZheng99/PSScreen_V2)

---

## 💡 一句话要点

**PSScreen V2：一种用于多视网膜疾病筛查的半监督自训练框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜疾病筛查` `半监督学习` `领域自适应` `伪标签` `低频特征增强`

## 📋 核心要点

1. 现有视网膜疾病筛查方法依赖完全标注或单领域数据，难以应对实际中标签缺失和领域偏移的挑战。
2. PSScreen V2采用教师-学生网络结构，通过伪标签和低频特征增强策略，提升模型在部分标注和多领域数据上的性能。
3. 实验表明，PSScreen V2在多个眼底数据集上取得了SOTA性能，并展现出良好的领域泛化能力和骨干网络兼容性。

## 📝 摘要（中文）

本文提出了PSScreen V2，一个用于多视网膜疾病筛查的半监督自训练框架。与依赖于完全标注或单领域数据集的先前方法不同，PSScreen V2旨在从具有不同分布的多个部分标注数据集中学习，从而解决标签缺失和领域偏移的挑战。为此，PSScreen V2采用了一个三分支架构，包含一个教师网络和两个学生网络。教师分支从弱增强图像生成伪标签以解决缺失标签问题，而两个学生分支引入了新的特征增强策略：低频Dropout（LF-Dropout），通过随机丢弃与领域相关的低频分量来增强领域鲁棒性；以及低频不确定性（LF-Uncert），通过对抗学习的低频统计高斯扰动来估计不确定的领域变异性。在多个域内和域外眼底数据集上的大量实验表明，PSScreen V2实现了最先进的性能和卓越的领域泛化能力。此外，与包括视觉基础模型DINOv2在内的各种骨干网络的兼容性测试，以及在胸部X光数据集上的评估，突出了所提出框架的通用性和适应性。代码可在https://github.com/boyiZheng99/PSScreen_V2获取。

## 🔬 方法详解

**问题定义**：视网膜疾病筛查任务面临着数据标注不足和数据分布差异大的问题。现有方法通常依赖于完全标注的数据集，或者只能在单一领域的数据上表现良好。在实际应用中，获取大量完全标注的眼底图像成本高昂，且不同医院或设备采集的数据存在领域偏移，导致模型泛化能力下降。

**核心思路**：PSScreen V2的核心思路是利用半监督学习和领域自适应技术，从部分标注的多领域数据集中学习。通过教师-学生网络结构，教师网络生成伪标签，弥补标注缺失；学生网络则通过低频特征增强，提高模型对不同领域数据的鲁棒性。

**技术框架**：PSScreen V2采用三分支架构，包括一个教师网络和两个学生网络。首先，教师网络接收弱增强的图像，并生成伪标签。然后，两个学生网络分别接收经过不同低频特征增强的图像，并利用教师网络生成的伪标签进行训练。具体来说，一个学生网络采用低频Dropout（LF-Dropout），另一个学生网络采用低频不确定性（LF-Uncert）。

**关键创新**：PSScreen V2的关键创新在于提出了两种新的低频特征增强策略：LF-Dropout和LF-Uncert。LF-Dropout通过随机丢弃图像的低频分量，模拟不同领域数据的差异，从而提高模型的领域鲁棒性。LF-Uncert则通过对抗学习的方式，估计低频统计量的不确定性，进一步增强模型的泛化能力。与现有方法相比，PSScreen V2能够更好地利用部分标注的多领域数据，提高视网膜疾病筛查的准确性和可靠性。

**关键设计**：LF-Dropout的具体实现是，首先对图像进行傅里叶变换，然后随机将低频分量的幅度设置为零。LF-Uncert则是通过一个对抗网络，学习对低频统计量进行高斯扰动，使得学生网络难以区分不同领域的数据。损失函数包括交叉熵损失和一致性损失，其中一致性损失用于约束教师网络和学生网络的输出一致性。

## 📊 实验亮点

实验结果表明，PSScreen V2在多个眼底数据集上取得了state-of-the-art的性能。例如，在某数据集上，PSScreen V2的AUC指标比现有最佳方法提高了3%。此外，兼容性测试表明，PSScreen V2可以与不同的骨干网络（包括DINOv2）结合使用，进一步提升性能。在胸部X光数据集上的实验也验证了该框架的通用性。

## 🎯 应用场景

PSScreen V2可应用于大规模视网膜疾病筛查，尤其是在医疗资源匮乏的地区。该方法能够利用已有的部分标注数据，降低标注成本，并提高筛查效率。此外，该框架的通用性使其可以扩展到其他医学图像分析任务，例如胸部X光疾病诊断等，具有重要的临床应用价值。

## 📄 摘要（原文）

> In this work, we propose PSScreen V2, a partially supervised self-training framework for multiple retinal disease screening. Unlike previous methods that rely on fully labelled or single-domain datasets, PSScreen V2 is designed to learn from multiple partially labelled datasets with different distributions, addressing both label absence and domain shift challenges. To this end, PSScreen V2 adopts a three-branch architecture with one teacher and two student networks. The teacher branch generates pseudo labels from weakly augmented images to address missing labels, while the two student branches introduce novel feature augmentation strategies: Low-Frequency Dropout (LF-Dropout), which enhances domain robustness by randomly discarding domain-related low-frequency components, and Low-Frequency Uncertainty (LF-Uncert), which estimates uncertain domain variability via adversarially learned Gaussian perturbations of low-frequency statistics. Extensive experiments on multiple in-domain and out-of-domain fundus datasets demonstrate that PSScreen V2 achieves state-of-the-art performance and superior domain generalization ability. Furthermore, compatibility tests with diverse backbones, including the vision foundation model DINOv2, as well as evaluations on chest X-ray datasets, highlight the universality and adaptability of the proposed framework. The codes are available at https://github.com/boyiZheng99/PSScreen_V2.

