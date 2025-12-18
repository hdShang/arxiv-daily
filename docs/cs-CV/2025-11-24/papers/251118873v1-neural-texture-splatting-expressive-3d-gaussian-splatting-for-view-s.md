---
layout: default
title: Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction
---

# Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18873" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18873v1</a>
  <a href="https://arxiv.org/pdf/2511.18873.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18873v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18873v1', 'Neural Texture Splatting: Expressive 3D Gaussian Splatting for View Synthesis, Geometry, and Dynamic Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Wang, Shaofei Wang, Marko Mihajlovic, Siyu Tang

**分类**: cs.CV, cs.GR

**发布日期**: 2025-11-24

**备注**: SIGGRAPH Asia 2025 (conference track), Project page: https://19reborn.github.io/nts/

---

## 💡 一句话要点

**提出神经纹理溅射（NTS），提升3D高斯溅射在视图合成、几何及动态重建任务上的性能。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经渲染` `3D高斯溅射` `新视角合成` `动态场景重建` `全局神经场`

## 📋 核心要点

1. 现有3D高斯溅射方法在建模局部变化时受限于3D高斯核，表达能力不足，限制了其在复杂场景重建中的应用。
2. 神经纹理溅射（NTS）通过全局神经场预测每个图元的局部外观和几何场，实现高效的全局信息交换和更强的泛化能力。
3. 实验表明，NTS在多种重建任务中显著提升了性能，并在多个基准测试中达到了最先进水平，尤其是在视角和时间依赖效果方面。

## 📝 摘要（中文）

3D高斯溅射(3DGS)已成为高质量新视角合成的主流方法，其众多变体将其适用性扩展到广泛的3D和4D场景重建任务。尽管如此，3DGS的表征能力仍然受到用于建模局部变化的3D高斯核的限制。最近的研究提出用额外的每图元容量来增强3DGS，例如每溅射纹理，以增强其表达能力。然而，这些每溅射纹理方法主要针对具有减少的高斯图元的密集新视角合成，并且当应用于更一般的重建场景时，其有效性往往会降低。本文旨在在稀疏和密集输入设置下，在包括新视角合成、几何和动态重建在内的广泛重建任务中，实现优于最先进的3DGS变体的具体性能改进。为此，我们引入了神经纹理溅射(NTS)。我们方法的核心是一个全局神经场(表示为三平面和神经解码器的混合)，它预测每个图元的局部外观和几何场。通过利用这种共享的全局表示来建模跨图元的局部纹理场，我们显著减少了模型大小并促进了有效的全局信息交换，展示了跨任务的强大泛化能力。此外，我们对局部纹理场的神经建模引入了富有表现力的视角和时间相关效果，这是现有方法未能考虑的关键方面。大量实验表明，神经纹理溅射始终改进模型并在多个基准测试中实现最先进的结果。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射方法使用3D高斯核来建模局部变化，表达能力有限，难以捕捉复杂的场景细节和视角、时间依赖性。此外，直接增加每图元纹理的方法虽然能提升表达能力，但在通用重建场景下效果不佳，且模型尺寸较大。

**核心思路**：NTS的核心在于使用一个全局神经场来预测每个高斯图元的局部外观和几何场。通过共享的全局表示，模型能够学习跨图元的局部纹理场，从而减少模型大小，并促进全局信息交换，增强泛化能力。同时，神经场的建模方式能够引入视角和时间依赖性，更好地捕捉动态场景的变化。

**技术框架**：NTS的整体框架包括以下几个关键模块：1) 3D高斯图元表示：使用3D高斯分布来表示场景中的点。2) 全局神经场：使用三平面和神经解码器的混合结构来表示全局神经场，该神经场负责预测每个高斯图元的局部外观和几何场。3) 局部纹理场预测：通过查询全局神经场，为每个高斯图元生成局部纹理场，用于渲染最终的图像。4) 渲染模块：将局部纹理场与高斯图元的属性结合，进行可微分渲染，生成最终的图像。

**关键创新**：NTS的关键创新在于使用全局神经场来建模局部纹理场。这种方法与直接为每个高斯图元分配纹理的方式不同，它能够利用全局信息来学习更有效的纹理表示，并减少模型大小。此外，神经场的建模方式能够引入视角和时间依赖性，这是现有方法所缺乏的。

**关键设计**：全局神经场使用三平面编码器和MLP解码器。三平面编码器将3D空间编码到三个正交的平面上，MLP解码器则根据三平面的特征来预测局部纹理场的属性。损失函数包括渲染损失（例如L1损失或感知损失）和正则化项，用于约束神经场的平滑性。

## 📊 实验亮点

实验结果表明，NTS在多个基准测试中显著提升了3D高斯溅射的性能。例如，在动态场景重建任务中，NTS相较于现有方法取得了显著的PSNR提升。此外，NTS在模型大小方面也具有优势，能够在保持甚至提升性能的同时，减少模型参数量，更易于部署和应用。

## 🎯 应用场景

神经纹理溅射（NTS）在三维重建、新视角合成、动态场景建模等领域具有广泛的应用前景。它可以用于创建更逼真、更具表现力的虚拟现实和增强现实体验，也可应用于机器人导航、自动驾驶等需要精确三维场景理解的领域。该技术有望推动相关领域的发展，并为用户带来更优质的视觉体验。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a leading approach for high-quality novel view synthesis, with numerous variants extending its applicability to a broad spectrum of 3D and 4D scene reconstruction tasks. Despite its success, the representational capacity of 3DGS remains limited by the use of 3D Gaussian kernels to model local variations. Recent works have proposed to augment 3DGS with additional per-primitive capacity, such as per-splat textures, to enhance its expressiveness. However, these per-splat texture approaches primarily target dense novel view synthesis with a reduced number of Gaussian primitives, and their effectiveness tends to diminish when applied to more general reconstruction scenarios. In this paper, we aim to achieve concrete performance improvement over state-of-the-art 3DGS variants across a wide range of reconstruction tasks, including novel view synthesis, geometry and dynamic reconstruction, under both sparse and dense input settings. To this end, we introduce Neural Texture Splatting (NTS). At the core of our approach is a global neural field (represented as a hybrid of a tri-plane and a neural decoder) that predicts local appearance and geometric fields for each primitive. By leveraging this shared global representation that models local texture fields across primitives, we significantly reduce model size and facilitate efficient global information exchange, demonstrating strong generalization across tasks. Furthermore, our neural modeling of local texture fields introduces expressive view- and time-dependent effects, a critical aspect that existing methods fail to account for. Extensive experiments show that Neural Texture Splatting consistently improves models and achieves state-of-the-art results across multiple benchmarks.

