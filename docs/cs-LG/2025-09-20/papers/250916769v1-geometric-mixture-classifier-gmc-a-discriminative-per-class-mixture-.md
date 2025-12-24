---
layout: default
title: "Geometric Mixture Classifier (GMC): A Discriminative Per-Class Mixture of Hyperplanes"
---

# Geometric Mixture Classifier (GMC): A Discriminative Per-Class Mixture of Hyperplanes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16769" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16769v1</a>
  <a href="https://arxiv.org/pdf/2509.16769.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16769v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16769v1', 'Geometric Mixture Classifier (GMC): A Discriminative Per-Class Mixture of Hyperplanes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prasanth K K, Shubham Sharma

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-20

**备注**: 21 pages, 6 figures, 14 tables

---

## 💡 一句话要点

**提出几何混合分类器(GMC)，用每类超平面混合模型解决多模态分类问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态分类` `超平面混合模型` `几何混合分类器` `软OR` `随机傅里叶特征` `可解释性` `高效推理`

## 📋 核心要点

1. 传统线性模型在处理多模态数据时性能受限，而高容量模型牺牲了解释性和效率。
2. GMC将每个类别表示为超平面的混合，通过软OR组合平面分数，并使用RFF进行非线性映射。
3. 实验表明，GMC在多个数据集上优于线性基线，并与RBF-SVM等模型具有竞争力，同时保持了高效的推理速度。

## 📝 摘要（中文）

许多现实世界的类别是多模态的，单个类别在特征空间中占据不相交的区域。传统的线性模型（如逻辑回归、线性SVM）使用单个全局超平面，在这种数据上表现不佳，而高容量方法（如核SVM、深度网络）虽然可以拟合多模态结构，但牺牲了解释性、需要更重的调参和更高的计算成本。我们提出了几何混合分类器（GMC），这是一种判别模型，将每个类别表示为超平面的混合。在每个类别中，GMC通过温度控制的软OR（log-sum-exp）组合平面分数，平滑地逼近最大值；在类别之间，标准softmax产生概率后验。GMC可以选择使用随机傅里叶特征（RFF）进行非线性映射，同时保持推理在平面和特征数量上的线性。我们提出的实用训练方法：几何感知k-means初始化、基于轮廓系数的平面预算、alpha退火、使用感知L2正则化、标签平滑和早停，使GMC即插即用。在合成多模态数据集（moons, circles, blobs, spirals）和表格/图像基准（iris, wine, WDBC, digits）上，GMC始终优于线性基线和k-NN，与RBF-SVM、随机森林和小型MLP具有竞争力，并通过每个平面和类别责任可视化提供几何自省。推理在平面和特征上线性缩放，使GMC对CPU友好，每个示例的延迟为个位数微秒，通常比RBF-SVM和紧凑型MLP更快。事后温度缩放将ECE从大约0.06降低到0.02。因此，GMC在准确性、可解释性和效率之间取得了良好的平衡：它比线性模型更具表现力，并且比核模型或深度模型更轻、更透明、更快。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态分类问题，即类别在特征空间中呈现多个不相交区域的情况。现有线性模型无法有效处理此类数据，而高容量模型（如深度学习）虽然可以拟合复杂分布，但计算成本高昂且缺乏可解释性。

**核心思路**：论文的核心思想是将每个类别表示为多个超平面的混合。每个超平面捕捉类别的一个模态，通过组合多个超平面的输出来实现对多模态数据的有效建模。这种方法在表达能力和计算效率之间取得了平衡。

**技术框架**：GMC的整体框架包括以下几个主要步骤：1) 使用几何感知k-means初始化超平面；2) 根据轮廓系数进行平面预算，控制模型复杂度；3) 使用温度控制的软OR（log-sum-exp）组合同一类别内不同超平面的输出；4) 使用softmax函数进行跨类别分类；5) 可选地使用随机傅里叶特征（RFF）进行非线性映射。

**关键创新**：GMC的关键创新在于使用超平面混合模型来表示每个类别，并采用软OR操作进行组合。这种方法既能捕捉多模态数据的复杂结构，又能保持模型的线性性和可解释性。此外，几何感知初始化和平面预算策略有助于提高模型的训练效率和泛化能力。

**关键设计**：GMC的关键设计包括：1) 几何感知k-means初始化，确保超平面能够覆盖类别的不同模态；2) 基于轮廓系数的平面预算，避免模型过拟合；3) 温度参数控制软OR的平滑程度，影响模型对不同模态的敏感度；4) 使用使用感知L2正则化，防止过拟合；5) 使用标签平滑和早停进一步提高泛化性能。

## 📊 实验亮点

GMC在合成多模态数据集和真实数据集上均取得了优异的性能。在多个数据集上，GMC优于线性基线和k-NN，并与RBF-SVM、随机森林和小型MLP具有竞争力。此外，GMC具有高效的推理速度，每个示例的延迟为个位数微秒，通常比RBF-SVM和紧凑型MLP更快。事后温度缩放将ECE从大约0.06降低到0.02。

## 🎯 应用场景

GMC适用于需要处理多模态数据的分类任务，例如图像识别、文本分类、生物信息学等。其高效的推理速度和良好的可解释性使其在资源受限的环境中也具有应用潜力。未来可以探索GMC在更复杂的多模态数据集上的应用，并研究如何自动确定超平面的数量和参数。

## 📄 摘要（原文）

> Many real world categories are multimodal, with single classes occupying disjoint regions in feature space. Classical linear models (logistic regression, linear SVM) use a single global hyperplane and perform poorly on such data, while high-capacity methods (kernel SVMs, deep nets) fit multimodal structure but at the expense of interpretability, heavier tuning, and higher computational cost. We propose the Geometric Mixture Classifier (GMC), a discriminative model that represents each class as a mixture of hyperplanes. Within each class, GMC combines plane scores via a temperature-controlled soft-OR (log-sum-exp), smoothly approximating the max; across classes, standard softmax yields probabilistic posteriors. GMC optionally uses Random Fourier Features (RFF) for nonlinear mappings while keeping inference linear in the number of planes and features. Our practical training recipe: geometry-aware k-means initialization, silhouette-based plane budgeting, alpha annealing, usage-aware L2 regularization, label smoothing, and early stopping, makes GMC plug-and-play. Across synthetic multimodal datasets (moons, circles, blobs, spirals) and tabular/image benchmarks (iris, wine, WDBC, digits), GMC consistently outperforms linear baselines and k-NN, is competitive with RBF-SVM, Random Forests, and small MLPs, and provides geometric introspection via per-plane and class responsibility visualizations. Inference scales linearly in planes and features, making GMC CPU-friendly, with single-digit microsecond latency per example, often faster than RBF-SVM and compact MLPs. Post-hoc temperature scaling reduces ECE from about 0.06 to 0.02. GMC thus strikes a favorable balance of accuracy, interpretability, and efficiency: it is more expressive than linear models and lighter, more transparent, and faster than kernel or deep models.

