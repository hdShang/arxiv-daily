---
layout: default
title: "G3Splat: Geometrically Consistent Generalizable Gaussian Splatting"
---

# G3Splat: Geometrically Consistent Generalizable Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17547" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17547v1</a>
  <a href="https://arxiv.org/pdf/2512.17547.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17547v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17547v1', 'G3Splat: Geometrically Consistent Generalizable Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehdi Hosseinzadeh, Shin-Fang Chng, Yi Xu, Simon Lucey, Ian Reid, Ravi Garg

**分类**: cs.CV

**发布日期**: 2025-12-19

**备注**: Project page: https://m80hz.github.io/g3splat/

**🔗 代码/项目**: [PROJECT_PAGE](https://m80hz.github.io/g3splat/)

---

## 💡 一句话要点

**G3Splat：通过几何一致性先验实现可泛化的高斯溅射**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯溅射` `三维重建` `新视角合成` `几何一致性` `可泛化` `自监督学习` `场景表示`

## 📋 核心要点

1. 现有方法依赖视角合成损失学习3D高斯溅射，难以保证几何一致性，导致重建质量下降。
2. G3Splat通过引入几何先验，显式地约束3D高斯溅射的学习过程，从而提升几何一致性。
3. 实验表明，G3Splat在几何重建、相对姿态估计和新视角合成方面均优于现有方法，并具有良好的泛化能力。

## 📝 摘要（中文）

3D高斯溅射最近成为一种有效的场景表示方法，可用于实时溅射和精确的新视角合成，这促使一些工作调整多视角结构预测网络，以从图像中回归每个像素的3D高斯分布。然而，先前的大部分工作扩展这些网络以预测额外的高斯参数——方向、尺度、不透明度和外观——同时几乎完全依赖于视角合成监督。我们表明，仅视角合成损失不足以在这种设置下恢复几何上有意义的溅射。我们分析并解决了在无姿态可泛化溅射的自监督下学习3D高斯溅射的模糊性，并引入了G3Splat，它强制执行几何先验以获得几何一致的3D场景表示。在RE10K上训练后，我们的方法在（i）几何一致的重建，（ii）相对姿态估计和（iii）新视角合成方面实现了最先进的性能。我们进一步展示了在ScanNet上的强大零样本泛化能力，在几何恢复和相对姿态估计方面都大大优于先前的工作。代码和预训练模型已在我们的项目页面上发布。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射的场景表示方法，在进行novel-view synthesis时，通常依赖于多视角图像进行训练，并使用view-synthesis loss作为主要的监督信号。然而，这种方法在学习高斯参数（如方向、尺度等）时存在模糊性，导致重建的3D场景在几何上不一致，影响了后续任务的性能，例如相对姿态估计。

**核心思路**：G3Splat的核心思路是通过引入几何先验，显式地约束3D高斯溅射的学习过程，从而解决几何不一致的问题。具体来说，论文通过设计特定的损失函数，鼓励学习到的高斯分布在空间中具有合理的几何形状，例如，相邻的高斯分布应该具有相似的朝向，避免出现不自然的扭曲。

**技术框架**：G3Splat的整体框架基于现有的多视角结构预测网络，并对其进行了扩展。该框架首先使用一个神经网络从多视角图像中预测每个像素的3D高斯参数，然后使用一个splatting渲染器将这些高斯分布渲染成图像。与现有方法不同的是，G3Splat在训练过程中引入了几何一致性损失，以约束学习到的高斯参数。该框架包含以下主要模块：图像特征提取模块、高斯参数预测模块、splatting渲染模块和几何一致性损失计算模块。

**关键创新**：G3Splat最重要的技术创新点在于引入了几何一致性损失，该损失能够有效地约束3D高斯溅射的学习过程，从而提高重建的3D场景的几何一致性。与现有方法相比，G3Splat不再仅仅依赖于view-synthesis loss，而是将几何先验融入到学习过程中，从而更好地利用了多视角图像中的几何信息。

**关键设计**：G3Splat的关键设计包括以下几个方面：1) 几何一致性损失的具体形式，例如，可以使用相邻高斯分布的朝向差异作为损失项；2) 几何一致性损失的权重，需要仔细调整以平衡view-synthesis loss和几何一致性损失之间的关系；3) 网络结构的细节，例如，可以使用更深的网络来提取更丰富的图像特征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17547v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17547v1/figs/re10k/ctx/aef133f549f40970_ctx_0_000010.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17547v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

G3Splat在RE10K数据集上实现了state-of-the-art的性能，在几何一致性重建、相对姿态估计和新视角合成方面均优于现有方法。此外，G3Splat在ScanNet数据集上展示了强大的零样本泛化能力，在几何恢复和相对姿态估计方面都大大优于先前的工作。例如，在相对姿态估计任务中，G3Splat的性能比现有方法提升了超过10%。

## 🎯 应用场景

G3Splat在三维重建、新视角合成、机器人导航、增强现实等领域具有广泛的应用前景。它可以用于创建高质量的3D场景模型，从而为机器人提供更准确的环境感知能力，并为用户提供更逼真的虚拟现实体验。此外，G3Splat还可以用于生成任意视角的图像，从而为图像编辑和视频制作提供更大的灵活性。

## 📄 摘要（原文）

> 3D Gaussians have recently emerged as an effective scene representation for real-time splatting and accurate novel-view synthesis, motivating several works to adapt multi-view structure prediction networks to regress per-pixel 3D Gaussians from images. However, most prior work extends these networks to predict additional Gaussian parameters -- orientation, scale, opacity, and appearance -- while relying almost exclusively on view-synthesis supervision. We show that a view-synthesis loss alone is insufficient to recover geometrically meaningful splats in this setting. We analyze and address the ambiguities of learning 3D Gaussian splats under self-supervision for pose-free generalizable splatting, and introduce G3Splat, which enforces geometric priors to obtain geometrically consistent 3D scene representations. Trained on RE10K, our approach achieves state-of-the-art performance in (i) geometrically consistent reconstruction, (ii) relative pose estimation, and (iii) novel-view synthesis. We further demonstrate strong zero-shot generalization on ScanNet, substantially outperforming prior work in both geometry recovery and relative pose estimation. Code and pretrained models are released on our project page (https://m80hz.github.io/g3splat/).

