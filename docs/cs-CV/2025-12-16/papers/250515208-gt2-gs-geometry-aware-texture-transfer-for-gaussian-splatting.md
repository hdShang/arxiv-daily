---
layout: default
title: GT2-GS: Geometry-aware Texture Transfer for Gaussian Splatting
---

# GT2-GS: Geometry-aware Texture Transfer for Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15208" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15208</a>
  <a href="https://arxiv.org/pdf/2505.15208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15208" onclick="toggleFavorite(this, '2505.15208', 'GT2-GS: Geometry-aware Texture Transfer for Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出GT2-GS，用于高斯溅射的几何感知纹理迁移，提升3D内容创作效率。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `高斯溅射` `纹理迁移` `几何感知` `3D重建` `风格迁移`

## 📋 核心要点

1. 现有3D纹理迁移方法忽略场景几何信息，导致迁移质量不高，难以满足高质量内容创作需求。
2. GT2-GS通过几何感知纹理增强和几何一致性损失，将纹理特征与几何信息对齐，实现高质量纹理迁移。
3. 实验结果表明，GT2-GS在纹理迁移效果和几何保持方面均优于现有方法，更符合人类视觉感知。

## 📝 摘要（中文）

本文提出了一种用于高斯溅射的几何感知纹理迁移框架GT^2-GS，旨在提升多媒体内容创作的效率。现有方法很少关注将图像纹理迁移到3D表示上。3D风格迁移方法虽然能够将抽象的艺术风格迁移到3D场景中，但往往忽略了场景的几何信息，导致难以实现高质量的3D纹理迁移结果。GT^2-GS通过匹配渲染视图中的纹理特征与几何信息，解决了纹理特征不足的问题，并提出了一个几何感知纹理增强模块来扩展纹理特征集。此外，还提出了一种几何一致性纹理损失，将纹理特征优化到场景表示中。该损失函数结合了相机姿态和场景的3D几何信息，实现了可控的、面向纹理的外观编辑。最后，引入了一种几何保持策略，通过在纹理迁移和几何校正阶段之间交替迭代，实现了学习纹理特征和保持几何完整性之间的平衡。大量实验表明了该方法的有效性和可控性，通过几何感知，该方法实现了更符合人类视觉感知的纹理迁移结果。

## 🔬 方法详解

**问题定义**：论文旨在解决将2D纹理高效、高质量地迁移到3D高斯溅射表示上的问题。现有方法，特别是3D风格迁移方法，通常忽略了场景的几何信息，导致纹理迁移结果与场景几何结构不一致，影响视觉效果。因此，如何利用几何信息指导纹理迁移，是本文要解决的核心问题。

**核心思路**：论文的核心思路是将纹理迁移过程与场景的几何信息紧密结合。通过几何感知的方式增强纹理特征，并利用几何一致性损失来约束纹理特征的学习，从而保证迁移后的纹理与场景的几何结构相符。此外，通过纹理迁移和几何校正的交替迭代，平衡纹理学习和几何保持。

**技术框架**：GT2-GS框架主要包含三个关键模块：几何感知纹理增强模块、几何一致性纹理损失和几何保持策略。首先，几何感知纹理增强模块用于扩展纹理特征集，弥补纹理特征的不足。然后，几何一致性纹理损失将纹理特征优化到场景表示中，确保纹理与几何结构一致。最后，几何保持策略通过交替迭代纹理迁移和几何校正，维持场景的几何完整性。

**关键创新**：该方法最重要的创新在于引入了几何感知的概念，将纹理迁移与场景的几何信息紧密结合。具体体现在：1）提出了几何感知纹理增强模块，利用几何信息指导纹理特征的提取和增强；2）设计了几何一致性纹理损失，利用相机姿态和3D几何信息约束纹理特征的学习。这种几何感知的策略是与现有方法最本质的区别。

**关键设计**：几何感知纹理增强模块的具体实现细节未知，但可以推测其利用了场景的深度信息或法向量信息来指导纹理特征的提取。几何一致性纹理损失可能采用了类似于光度一致性的损失函数，但加入了相机姿态和3D几何信息的约束项。几何保持策略的具体迭代次数和校正方法未知，但其目的是为了防止纹理迁移过程中对原始几何结构的过度破坏。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.15208/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.15208/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.15208/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GT2-GS在纹理迁移效果和几何保持方面均优于现有方法。通过几何感知，该方法能够生成更符合人类视觉感知的纹理迁移结果。具体的性能数据和对比基线在论文中进行了详细的展示，证明了该方法的有效性和优越性。

## 🎯 应用场景

该研究成果可广泛应用于3D内容创作、虚拟现实、增强现实等领域。例如，可以快速将照片纹理迁移到3D模型上，生成逼真的3D场景；也可以用于游戏开发中，快速创建具有特定纹理风格的3D角色和场景。该方法有望降低3D内容创作的门槛，提高创作效率。

## 📄 摘要（原文）

> Transferring 2D textures to 3D modalities is of great significance for improving the efficiency of multimedia content creation. Existing approaches have rarely focused on transferring image textures onto 3D representations. 3D style transfer methods are capable of transferring abstract artistic styles to 3D scenes. However, these methods often overlook the geometric information of the scene, which makes it challenging to achieve high-quality 3D texture transfer results. In this paper, we present GT^2-GS, a geometry-aware texture transfer framework for gaussian splitting. From the perspective of matching texture features with geometric information in rendered views, we identify the issue of insufficient texture features and propose a geometry-aware texture augmentation module to expand the texture feature set. Moreover, a geometry-consistent texture loss is proposed to optimize texture features into the scene representation. This loss function incorporates both camera pose and 3D geometric information of the scene, enabling controllable texture-oriented appearance editing. Finally, a geometry preservation strategy is introduced. By alternating between the texture transfer and geometry correction stages over multiple iterations, this strategy achieves a balance between learning texture features and preserving geometric integrity. Extensive experiments demonstrate the effectiveness and controllability of our method. Through geometric awareness, our approach achieves texture transfer results that better align with human visual perception. Our homepage is available atthis https URL.

