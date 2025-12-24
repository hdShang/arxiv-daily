---
layout: default
title: "AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views"
---

# AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23716" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23716v2</a>
  <a href="https://arxiv.org/pdf/2505.23716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23716v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23716v2', 'AnySplat: Feed-forward 3D Gaussian Splatting from Unconstrained Views')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lihan Jiang, Yucheng Mao, Linning Xu, Tao Lu, Kerui Ren, Yichen Jin, Xudong Xu, Mulin Yu, Jiangmiao Pang, Feng Zhao, Dahua Lin, Bo Dai

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-09-15)

**备注**: Project page: https://city-super.github.io/anysplat/

**🔗 代码/项目**: [PROJECT_PAGE](https://city-super.github.io/anysplat/)

---

## 💡 一句话要点

**提出AnySplat以解决无标定视图下的新视图合成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新视图合成` `3D高斯原语` `无标定视图` `神经渲染` `实时合成`

## 📋 核心要点

1. 现有方法通常依赖于已知的相机姿态和复杂的逐场景优化，限制了其在无标定视图下的应用。
2. AnySplat通过一次前向传递生成3D高斯原语，简化了新视图合成的过程，避免了对相机姿态的依赖。
3. 在零-shot评估中，AnySplat在稀疏和密集视图场景中表现优异，超越了现有无姿态方法，并显著降低了渲染延迟。

## 📝 摘要（中文）

我们介绍了AnySplat，这是一种用于从无标定图像集合中进行新视图合成的前馈网络。与传统的神经渲染管道需要已知的相机姿态和逐场景优化不同，AnySplat在一次前向传递中预测所有内容。该模型生成一组3D高斯原语，编码场景几何和外观，同时为每个输入图像提供相应的相机内外参数。该统一设计能够轻松扩展到随意捕获的多视图数据集，无需任何姿态注释。在广泛的零-shot评估中，AnySplat在稀疏和密集视图场景中匹配了姿态感知基线的质量，同时超越了现有的无姿态方法。此外，与基于优化的神经场相比，它显著降低了渲染延迟，使得在无约束捕获设置下实现实时新视图合成成为可能。

## 🔬 方法详解

**问题定义**：论文旨在解决在无标定视图下进行新视图合成的挑战。现有方法通常需要已知的相机姿态和复杂的优化过程，限制了其在实际应用中的灵活性和效率。

**核心思路**：AnySplat的核心思想是通过一次前向传递生成3D高斯原语，这些原语同时编码了场景的几何形状和外观信息，从而避免了对相机姿态的依赖。

**技术框架**：该方法的整体架构包括输入图像的处理、3D高斯原语的生成以及相机内外参数的预测。所有这些步骤在一个统一的前馈网络中完成，极大地提高了效率。

**关键创新**：AnySplat的最大创新在于其能够在没有姿态注释的情况下，直接从无标定图像中生成高质量的新视图合成，显著简化了传统方法的复杂性。

**关键设计**：在网络设计中，AnySplat采用了特定的损失函数来优化生成的高斯原语的质量，并通过精心选择的网络结构来提高模型的表达能力和渲染速度。具体的参数设置和网络层次结构在论文中有详细描述。

## 📊 实验亮点

在实验中，AnySplat在稀疏和密集视图场景中均表现出色，其生成的图像质量与姿态感知基线相当，同时在渲染延迟上显著降低，达到实时合成的标准。这一成果展示了其在无标定视图合成中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实以及计算机图形学等领域。通过实现实时的新视图合成，AnySplat可以为用户提供更为沉浸和互动的体验，推动相关技术的发展和应用。未来，随着数据采集技术的进步，AnySplat有望在更多实际场景中得到应用。

## 📄 摘要（原文）

> We introduce AnySplat, a feed forward network for novel view synthesis from uncalibrated image collections. In contrast to traditional neural rendering pipelines that demand known camera poses and per scene optimization, or recent feed forward methods that buckle under the computational weight of dense views, our model predicts everything in one shot. A single forward pass yields a set of 3D Gaussian primitives encoding both scene geometry and appearance, and the corresponding camera intrinsics and extrinsics for each input image. This unified design scales effortlessly to casually captured, multi view datasets without any pose annotations. In extensive zero shot evaluations, AnySplat matches the quality of pose aware baselines in both sparse and dense view scenarios while surpassing existing pose free approaches. Moreover, it greatly reduce rendering latency compared to optimization based neural fields, bringing real time novel view synthesis within reach for unconstrained capture settings.Project page: https://city-super.github.io/anysplat/

