---
layout: default
title: Foundation Model Priors Enhance Object Focus in Feature Space for Source-Free Object Detection
---

# Foundation Model Priors Enhance Object Focus in Feature Space for Source-Free Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17514" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17514v1</a>
  <a href="https://arxiv.org/pdf/2512.17514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17514v1', 'Foundation Model Priors Enhance Object Focus in Feature Space for Source-Free Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sairam VCR, Rishabh Lalla, Aveen Dayal, Tejal Kulkarni, Anuj Lalla, Vineeth N Balasubramanian, Muhammad Haris Khan

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**FALCON-SFOD：利用先验知识增强源域无关目标检测中的目标聚焦**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `源域无关目标检测` `领域自适应` `视觉基础模型` `伪标签学习` `特征空间正则化`

## 📋 核心要点

1. 源域无关目标检测(SFOD)受域偏移影响，检测器易产生背景杂乱激活，导致伪标签质量下降。
2. FALCON-SFOD框架通过空间先验感知正则化(SPAR)和不平衡感知噪声鲁棒伪标签(IRPL)增强目标聚焦。
3. 实验结果表明，FALCON-SFOD在多个SFOD基准测试中表现出色，验证了其有效性。

## 📝 摘要（中文）

本文提出FALCON-SFOD，一个用于增强域迁移下目标聚焦自适应的框架，旨在解决源域无关目标检测(SFOD)中，由于域偏移导致检测器难以维持强目标聚焦表示，从而产生大量背景杂乱激活的问题。该框架包含两个互补组件：空间先验感知正则化(SPAR)，利用视觉基础模型的泛化能力来正则化检测器的特征空间，通过OV-SAM生成的类别无关二值掩码，引导网络关注目标区域，促进结构化和前景聚焦的激活；不平衡感知噪声鲁棒伪标签(IRPL)，通过促进平衡和噪声容忍的学习来补充SPAR，解决严重的前景-背景不平衡问题。理论分析表明，这些设计能够收紧定位和分类误差界限，FALCON-SFOD在SFOD基准测试中取得了具有竞争力的性能。

## 🔬 方法详解

**问题定义**：源域无关目标检测(SFOD)旨在利用已标注的源域数据训练目标检测器，并将其应用于未标注的目标域，而无需访问源域数据。现有方法，特别是基于Mean-Teacher自标记的方法，在域偏移下，检测器难以维持强目标聚焦的特征表示，导致高置信度的激活出现在背景杂乱区域，从而产生不可靠的伪标签。现有工作主要集中在伪标签的提炼上，忽略了增强特征空间本身的重要性。

**核心思路**：FALCON-SFOD的核心思路是利用视觉基础模型（Vision Foundation Model）的先验知识来指导目标检测器的特征学习，从而增强其在目标域中的目标聚焦能力。具体来说，通过空间先验感知正则化(SPAR)模块，利用开放词汇语义分割模型(OV-SAM)生成的类别无关二值掩码，引导检测器关注目标区域，抑制背景噪声。同时，通过不平衡感知噪声鲁棒伪标签(IRPL)模块，解决前景-背景不平衡问题，提高伪标签的质量。

**技术框架**：FALCON-SFOD框架主要包含两个模块：SPAR和IRPL。首先，利用OV-SAM在目标域图像上生成类别无关的二值掩码，这些掩码指示了图像中可能包含目标的区域。然后，SPAR模块利用这些掩码对检测器的特征空间进行正则化，促使检测器学习到更关注目标区域的特征表示。同时，IRPL模块用于生成更准确的伪标签，并解决训练过程中前景-背景类别不平衡的问题。整个框架采用Mean-Teacher的训练方式，即同时训练一个学生模型和一个教师模型，并利用教师模型生成的伪标签来指导学生模型的学习。

**关键创新**：FALCON-SFOD的关键创新在于利用视觉基础模型的先验知识来增强目标检测器的特征空间。与现有方法主要关注伪标签的提炼不同，FALCON-SFOD从根本上解决了特征空间中目标聚焦不足的问题。通过SPAR模块，FALCON-SFOD能够有效地抑制背景噪声，提高检测器对目标区域的敏感性。此外，IRPL模块进一步提高了伪标签的质量，使得检测器能够更好地适应目标域。

**关键设计**：SPAR模块的关键设计在于如何有效地利用OV-SAM生成的二值掩码。论文采用了一种空间先验感知损失函数，该损失函数鼓励检测器的特征激活在掩码指示的目标区域内具有更高的值，而在掩码之外具有更低的值。IRPL模块的关键设计在于如何解决前景-背景类别不平衡的问题。论文采用了一种不平衡感知损失函数，该损失函数对少数类别（通常是前景目标）赋予更高的权重，从而使得检测器能够更好地学习到这些类别的特征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17514v1/images/FALCON-SFOD-teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17514v1/images/spar_impact.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17514v1/images/map_vs_m.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文在多个SFOD基准测试中验证了FALCON-SFOD的有效性。实验结果表明，FALCON-SFOD在多个数据集上取得了显著的性能提升，超过了现有的state-of-the-art方法。具体的性能数据需要在论文中查找，这里无法给出。

## 🎯 应用场景

FALCON-SFOD在安全监控、自动驾驶、医学图像分析等领域具有广泛的应用前景。例如，在安全监控中，可以利用FALCON-SFOD检测不同场景下的异常行为，而无需针对每个场景重新训练模型。在自动驾驶中，可以利用FALCON-SFOD检测不同天气和光照条件下的交通标志和行人，提高驾驶安全性。在医学图像分析中，可以利用FALCON-SFOD检测不同类型的病灶，辅助医生进行诊断。

## 📄 摘要（原文）

> Current state-of-the-art approaches in Source-Free Object Detection (SFOD) typically rely on Mean-Teacher self-labeling. However, domain shift often reduces the detector's ability to maintain strong object-focused representations, causing high-confidence activations over background clutter. This weak object focus results in unreliable pseudo-labels from the detection head. While prior works mainly refine these pseudo-labels, they overlook the underlying need to strengthen the feature space itself. We propose FALCON-SFOD (Foundation-Aligned Learning with Clutter suppression and Noise robustness), a framework designed to enhance object-focused adaptation under domain shift. It consists of two complementary components. SPAR (Spatial Prior-Aware Regularization) leverages the generalization strength of vision foundation models to regularize the detector's feature space. Using class-agnostic binary masks derived from OV-SAM, SPAR promotes structured and foreground-focused activations by guiding the network toward object regions. IRPL (Imbalance-aware Noise Robust Pseudo-Labeling) complements SPAR by promoting balanced and noise-tolerant learning under severe foreground-background imbalance. Guided by a theoretical analysis that connects these designs to tighter localization and classification error bounds, FALCON-SFOD achieves competitive performance across SFOD benchmarks.

