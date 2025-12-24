---
layout: default
title: "PointAD+: Learning Hierarchical Representations for Zero-shot 3D Anomaly Detection"
---

# PointAD+: Learning Hierarchical Representations for Zero-shot 3D Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03277" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03277v5</a>
  <a href="https://arxiv.org/pdf/2509.03277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03277v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03277v5', 'PointAD+: Learning Hierarchical Representations for Zero-shot 3D Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qihang Zhou, Shibo He, Jiangtao Yan, Wenchao Meng, Jiming Chen

**分类**: cs.CV

**发布日期**: 2025-09-03 (更新: 2025-11-24)

**备注**: Submitted to TPAMI

---

## 💡 一句话要点

**PointAD+：学习分层表示，实现零样本3D异常检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D异常检测` `零样本学习` `分层表示学习` `对比学习` `点云处理`

## 📋 核心要点

1. 现有3D异常检测方法难以泛化到未见过的物体类别，尤其是在类别语义高度多样的情况下，缺乏有效的零样本学习能力。
2. PointAD+通过分层表示学习，结合隐式渲染像素异常和显式空间几何异常，并利用跨层次对比对齐促进二者交互，提升泛化能力。
3. 实验结果表明，PointAD+在零样本3D异常检测任务中表现出色，能够有效检测和分割具有多样化类别语义的未见物体的异常。

## 📝 摘要（中文）

本文旨在将CLIP强大的2D泛化能力迁移到3D领域，以识别具有高度多样化类别语义的未见物体的3D异常。为此，我们提出了一个统一的框架，通过利用点和像素级别的信息来全面检测和分割3D异常。我们首先设计了PointAD，它利用点-像素对应关系，通过其相关的渲染像素表示来表示3D异常。这种方法被称为隐式3D表示，因为它只关注渲染像素异常，而忽略了点云中固有的空间关系。然后，我们提出了PointAD+，通过引入显式3D表示来进一步拓宽对3D异常的解释，强调空间异常以揭示异常的空间关系。因此，我们提出了G-aggregation来引入几何信息，使聚合的点表示具有空间感知能力。为了同时捕获渲染和空间异常，PointAD+提出了分层表示学习，将隐式和显式异常语义整合到分层文本提示中：渲染层的渲染提示和几何层的几何提示。进一步引入了跨层次对比对齐，以促进渲染层和几何层之间的交互，从而促进相互异常学习。最后，PointAD+集成了来自两层的异常语义，以捕获广义的异常语义。在测试过程中，PointAD+可以以即插即用的方式集成RGB信息，并进一步提高其检测性能。大量的实验表明，PointAD+在具有高度多样化类别语义的未见物体上的ZS 3D异常检测方面具有优越性，实现了对异常的整体理解。

## 🔬 方法详解

**问题定义**：现有的3D异常检测方法在面对未见过的物体类别时，泛化能力不足。尤其是在类别语义高度多样的情况下，这些方法难以有效地识别和分割3D场景中的异常。主要痛点在于缺乏利用先验知识和有效结合不同模态信息的能力，导致模型对新物体的异常判断能力较弱。

**核心思路**：PointAD+的核心思路是将CLIP强大的2D视觉-语言预训练模型的泛化能力迁移到3D异常检测任务中。通过建立3D点云和2D渲染图像之间的对应关系，并结合空间几何信息，模型能够学习到更鲁棒的异常表示，从而实现零样本的异常检测。关键在于同时考虑渲染像素级别的异常和空间几何结构的异常，并将二者融合。

**技术框架**：PointAD+的整体框架包含以下几个主要模块：1) **PointAD模块**：利用点-像素对应关系，通过渲染像素表示3D异常（隐式3D表示）。2) **G-aggregation模块**：引入几何信息，使聚合的点表示具有空间感知能力（显式3D表示）。3) **分层表示学习模块**：将隐式和显式异常语义整合到分层文本提示中，包括渲染提示和几何提示。4) **跨层次对比对齐模块**：促进渲染层和几何层之间的交互，从而促进相互异常学习。5) **异常语义融合模块**：集成了来自两层的异常语义，以捕获广义的异常语义。

**关键创新**：PointAD+的关键创新在于其分层表示学习和跨层次对比对齐机制。通过同时考虑渲染像素级别的异常和空间几何结构的异常，并利用对比学习促进二者之间的信息交互，模型能够学习到更全面、更鲁棒的异常表示。与现有方法相比，PointAD+不仅考虑了渲染像素的异常，还关注了空间几何结构的异常，从而能够更准确地检测和分割3D异常。

**关键设计**：在分层表示学习中，针对渲染层和几何层分别设计了渲染提示和几何提示，用于指导模型学习相应的异常语义。跨层次对比对齐通过对比学习损失函数，促使渲染层和几何层学习到相似的异常表示。G-aggregation模块的具体实现方式（例如，使用哪种图神经网络）以及损失函数的具体形式（例如，InfoNCE损失）是影响模型性能的关键设计。

## 📊 实验亮点

实验结果表明，PointAD+在零样本3D异常检测任务中取得了显著的性能提升。具体来说，PointAD+在多个数据集上超越了现有的基线方法，尤其是在处理具有高度多样化类别语义的未见物体时，其性能优势更加明显。此外，通过集成RGB信息，PointAD+的检测性能得到了进一步的提升，验证了其即插即用的特性。

## 🎯 应用场景

PointAD+在工业质检、自动驾驶、医疗诊断等领域具有广泛的应用前景。例如，在工业质检中，可以用于检测产品表面的缺陷或异常；在自动驾驶中，可以用于识别道路上的障碍物或异常情况；在医疗诊断中，可以用于检测医学图像中的病灶或异常组织。该研究的实际价值在于提高了3D异常检测的准确性和泛化能力，为相关领域的智能化应用提供了技术支持。未来，可以进一步探索如何将PointAD+与其他模态的信息（如文本、声音）相结合，以实现更全面的异常检测。

## 📄 摘要（原文）

> In this paper, we aim to transfer CLIP's robust 2D generalization capabilities to identify 3D anomalies across unseen objects of highly diverse class semantics. To this end, we propose a unified framework to comprehensively detect and segment 3D anomalies by leveraging both point- and pixel-level information. We first design PointAD, which leverages point-pixel correspondence to represent 3D anomalies through their associated rendering pixel representations. This approach is referred to as implicit 3D representation, as it focuses solely on rendering pixel anomalies but neglects the inherent spatial relationships within point clouds. Then, we propose PointAD+ to further broaden the interpretation of 3D anomalies by introducing explicit 3D representation, emphasizing spatial abnormality to uncover abnormal spatial relationships. Hence, we propose G-aggregation to involve geometry information to enable the aggregated point representations spatially aware. To simultaneously capture rendering and spatial abnormality, PointAD+ proposes hierarchical representation learning, incorporating implicit and explicit anomaly semantics into hierarchical text prompts: rendering prompts for the rendering layer and geometry prompts for the geometry layer. A cross-hierarchy contrastive alignment is further introduced to promote the interaction between the rendering and geometry layers, facilitating mutual anomaly learning. Finally, PointAD+ integrates anomaly semantics from both layers to capture the generalized anomaly semantics. During the test, PointAD+ can integrate RGB information in a plug-and-play manner and further improve its detection performance. Extensive experiments demonstrate the superiority of PointAD+ in ZS 3D anomaly detection across unseen objects with highly diverse class semantics, achieving a holistic understanding of abnormality.

