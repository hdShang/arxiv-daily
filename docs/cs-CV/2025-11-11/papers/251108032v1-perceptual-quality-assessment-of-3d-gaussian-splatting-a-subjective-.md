---
layout: default
title: "Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric"
---

# Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08032" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08032v1</a>
  <a href="https://arxiv.org/pdf/2511.08032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.08032v1', 'Perceptual Quality Assessment of 3D Gaussian Splatting: A Subjective Dataset and Prediction Metric')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaolin Wan, Yining Diao, Jingqi Xu, Hao Wang, Zhiyang Li, Xiaopeng Fan, Wangmeng Zuo, Debin Zhao

**分类**: cs.CV

**发布日期**: 2025-11-11

**🔗 代码/项目**: [GITHUB](https://github.com/diaoyn/3DGSQA)

---

## 💡 一句话要点

**提出3DGS-QA数据集与无参考质量评估模型，解决3D高斯溅射感知质量评估问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `质量评估` `感知质量` `无参考评估` `主观数据集`

## 📋 核心要点

1. 现有3DGS质量评估缺乏系统研究，尤其是在各种重建条件下的感知质量评估。
2. 提出一种无需参考的质量预测模型，直接作用于3D高斯基元，提取空间和光度线索。
3. 实验表明，该方法在3DGS内容评估中表现出优越的性能和鲁棒性。

## 📝 摘要（中文）

随着3D可视化的快速发展，3D高斯溅射(3DGS)已成为实时、高保真渲染的主流技术。虽然之前的研究强调了算法性能和视觉保真度，但3DGS渲染内容的感知质量，尤其是在不同的重建条件下，在很大程度上仍未被探索。实际上，视点稀疏性、有限的训练迭代次数、点降采样、噪声和颜色失真等因素会显著降低视觉质量，但它们对感知的影响尚未得到系统研究。为了弥补这一差距，我们提出了3DGS-QA，这是第一个针对3DGS的主观质量评估数据集。它包含15种对象类型的225个降级重建，从而能够对常见失真因素进行受控研究。基于此数据集，我们引入了一种无需参考的质量预测模型，该模型直接在原生3D高斯基元上运行，而无需渲染图像或ground-truth参考。我们的模型从高斯表示中提取空间和光度线索，以结构感知的方式估计感知质量。我们进一步对现有的质量评估方法进行了基准测试，包括传统方法和基于学习的方法。实验结果表明，我们的方法始终能获得优越的性能，突出了其在3DGS内容评估中的鲁棒性和有效性。数据集和代码已在https://github.com/diaoyn/3DGSQA上公开发布，以促进未来在3DGS质量评估方面的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决3D高斯溅射（3DGS）渲染结果的感知质量评估问题。现有方法要么依赖于渲染后的图像进行评估，要么需要ground-truth作为参考，无法直接对3D高斯基元进行质量评估，且缺乏针对3DGS特定失真因素的系统研究。这些痛点限制了3DGS在实际应用中的质量控制和优化。

**核心思路**：论文的核心思路是直接从3D高斯基元中提取特征，构建一个无需参考的质量评估模型。该模型通过分析高斯分布的空间和光度属性，来预测人类对渲染结果的感知质量。这种方法避免了渲染过程，提高了评估效率，并且能够更好地捕捉3DGS特有的失真模式。

**技术框架**：该方法主要包含以下几个阶段：1) 构建3DGS-QA数据集，包含不同对象和不同失真程度的3DGS重建结果，并进行主观质量评估；2) 设计特征提取模块，从每个高斯基元中提取空间（如位置、尺度、旋转）和光度（如颜色、透明度）特征；3) 构建质量预测模型，利用提取的特征预测感知质量得分。该模型可以使用机器学习或深度学习方法进行训练。

**关键创新**：该方法最重要的技术创新点在于提出了一个直接作用于3D高斯基元的无需参考质量评估模型。与传统的基于图像的质量评估方法相比，该方法能够更有效地捕捉3DGS特有的失真模式，并且避免了渲染过程，提高了评估效率。此外，3DGS-QA数据集的构建也为该领域的研究提供了宝贵资源。

**关键设计**：关键设计包括：1) 特征提取模块的设计，需要选择能够有效表征高斯基元质量的特征；2) 质量预测模型的选择和训练，需要选择合适的模型结构和损失函数，以实现准确的质量预测；3) 数据集的构建，需要覆盖不同的对象和失真程度，以保证模型的泛化能力。具体的参数设置、损失函数和网络结构等细节在论文中应该有详细描述。

## 📊 实验亮点

实验结果表明，该方法在3DGS质量评估任务中取得了优越的性能，显著优于现有的传统和基于学习的质量评估方法。具体而言，该方法在3DGS-QA数据集上取得了最高的预测准确率和一致性，证明了其在3DGS内容评估中的鲁棒性和有效性。具体的性能提升数据需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于3D内容创作、3D重建和实时渲染等领域。它可以帮助开发者评估和优化3DGS渲染结果的质量，提高用户体验。此外，该方法还可以用于自动化的3D内容质量控制，例如在3D模型库中筛选高质量的模型。未来，该研究可以扩展到其他基于点的渲染技术，并与其他质量评估方法相结合，进一步提高3D内容质量评估的准确性和效率。

## 📄 摘要（原文）

> With the rapid advancement of 3D visualization, 3D Gaussian Splatting (3DGS) has emerged as a leading technique for real-time, high-fidelity rendering. While prior research has emphasized algorithmic performance and visual fidelity, the perceptual quality of 3DGS-rendered content, especially under varying reconstruction conditions, remains largely underexplored. In practice, factors such as viewpoint sparsity, limited training iterations, point downsampling, noise, and color distortions can significantly degrade visual quality, yet their perceptual impact has not been systematically studied. To bridge this gap, we present 3DGS-QA, the first subjective quality assessment dataset for 3DGS. It comprises 225 degraded reconstructions across 15 object types, enabling a controlled investigation of common distortion factors. Based on this dataset, we introduce a no-reference quality prediction model that directly operates on native 3D Gaussian primitives, without requiring rendered images or ground-truth references. Our model extracts spatial and photometric cues from the Gaussian representation to estimate perceived quality in a structure-aware manner. We further benchmark existing quality assessment methods, spanning both traditional and learning-based approaches. Experimental results show that our method consistently achieves superior performance, highlighting its robustness and effectiveness for 3DGS content evaluation. The dataset and code are made publicly available at https://github.com/diaoyn/3DGSQA to facilitate future research in 3DGS quality assessment.

