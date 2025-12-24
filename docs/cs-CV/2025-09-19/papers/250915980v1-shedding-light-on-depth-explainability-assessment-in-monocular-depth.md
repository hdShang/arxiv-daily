---
layout: default
title: "Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation"
---

# Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15980" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15980v1</a>
  <a href="https://arxiv.org/pdf/2509.15980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15980v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15980v1', 'Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lorenzo Cirillo, Claudio Schiavella, Lorenzo Papa, Paolo Russo, Irene Amerini

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-19

**备注**: 8 pages, 3 figures, 2 tables. This paper has been accepted at the International Joint Conference on Neural Networks (IJCNN) 2025

---

## 💡 一句话要点

**单目深度估计可解释性研究：提出Attribution Fidelity评估解释可靠性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `单目深度估计` `可解释性` `特征归因` `Saliency Maps` `Integrated Gradients` `Attribution Fidelity` `深度学习` `模型评估`

## 📋 核心要点

1. 单目深度估计可解释性不足，阻碍了其在安全攸关场景中的应用，需要深入理解模型决策过程。
2. 通过分析特征归因方法在MDE模型中的表现，并提出Attribution Fidelity指标，评估解释的可靠性。
3. 实验表明Saliency Maps和Integrated Gradients在不同模型上表现各异，Attribution Fidelity能有效识别解释失效情况。

## 📝 摘要（中文）

本文致力于研究单目深度估计(MDE)网络的可解释性，旨在理解输入图像到预测深度图的映射过程。尽管MDE已广泛应用于现实场景，但其可解释性仍未得到充分探索。本文研究了三种特征归因方法：Saliency Maps、Integrated Gradients和Attention Rollout，应用于两种计算复杂度不同的MDE模型：轻量级网络METER和深度网络PixelFormer。通过选择性地扰动由可解释性方法识别的最相关和最不相关的像素，并分析这些扰动对模型输出的影响，来评估生成的可视化解释的质量。此外，针对现有评估指标在衡量MDE可视化解释有效性方面的局限性，本文提出了一种新的指标：Attribution Fidelity，通过评估特征归因与预测深度图的一致性来衡量其可靠性。实验结果表明，Saliency Maps和Integrated Gradients在分别突出显示轻量级和深度MDE模型的最重要输入特征方面表现良好。此外，Attribution Fidelity能够有效识别可解释性方法未能产生可靠可视化图的情况，即使在传统指标可能显示令人满意的结果的情况下。

## 🔬 方法详解

**问题定义**：单目深度估计(MDE)在许多实际应用中发挥作用，但其内部决策过程如同黑盒，缺乏透明度和可解释性。现有方法难以有效评估MDE模型的可解释性，尤其是在可视化解释的可靠性方面，传统指标可能无法准确反映解释的质量。因此，如何理解MDE网络如何从输入图像预测深度图，并评估解释的可靠性，是本文要解决的核心问题。

**核心思路**：本文的核心思路是通过特征归因方法来突出显示输入图像中对深度预测贡献最大的区域，并设计新的评估指标来衡量这些归因的可靠性。通过扰动图像中的关键区域，观察模型输出的变化，从而验证归因的有效性。此外，提出Attribution Fidelity指标，直接评估归因与预测深度图的一致性，从而更全面地评估解释的可靠性。

**技术框架**：本文的技术框架主要包括以下几个步骤：1) 选择两种具有代表性的MDE模型（METER和PixelFormer）；2) 应用三种特征归因方法（Saliency Maps、Integrated Gradients和Attention Rollout）生成可视化解释；3) 通过扰动输入图像的关键区域来评估解释的有效性；4) 提出并使用Attribution Fidelity指标评估解释的可靠性。整个流程旨在系统地分析和评估MDE模型的可解释性。

**关键创新**：本文的关键创新在于提出了Attribution Fidelity指标，用于评估MDE模型可视化解释的可靠性。与传统的评估指标不同，Attribution Fidelity直接衡量特征归因与预测深度图之间的一致性，能够更准确地反映解释的质量。此外，本文系统地比较了不同特征归因方法在不同MDE模型上的表现，为选择合适的可解释性方法提供了指导。

**关键设计**：Attribution Fidelity的计算方式是基于特征归因图和预测深度图之间的相关性。具体来说，首先对特征归因图和深度图进行归一化，然后计算它们之间的皮尔逊相关系数。相关系数越高，说明特征归因与深度预测越一致，解释的可靠性越高。此外，在扰动实验中，选择性地遮挡或保留由特征归因方法识别的最重要和最不重要的像素，并观察模型输出的变化，从而评估解释的有效性。

## 📊 实验亮点

实验结果表明，Saliency Maps在轻量级模型METER上表现良好，而Integrated Gradients在深度模型PixelFormer上更有效。Attribution Fidelity能够有效识别传统指标可能无法检测到的解释失效情况。例如，在某些情况下，即使扰动实验显示了令人满意的结果，Attribution Fidelity仍然可以检测到特征归因与深度预测之间的不一致性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、三维重建等领域。通过提高单目深度估计的可解释性，可以增强人们对模型预测结果的信任，从而促进其在安全攸关场景中的应用。未来的研究可以进一步探索更有效的可解释性方法，并将其应用于更复杂的深度估计模型。

## 📄 摘要（原文）

> Explainable artificial intelligence is increasingly employed to understand the decision-making process of deep learning models and create trustworthiness in their adoption. However, the explainability of Monocular Depth Estimation (MDE) remains largely unexplored despite its wide deployment in real-world applications. In this work, we study how to analyze MDE networks to map the input image to the predicted depth map. More in detail, we investigate well-established feature attribution methods, Saliency Maps, Integrated Gradients, and Attention Rollout on different computationally complex models for MDE: METER, a lightweight network, and PixelFormer, a deep network. We assess the quality of the generated visual explanations by selectively perturbing the most relevant and irrelevant pixels, as identified by the explainability methods, and analyzing the impact of these perturbations on the model's output. Moreover, since existing evaluation metrics can have some limitations in measuring the validity of visual explanations for MDE, we additionally introduce the Attribution Fidelity. This metric evaluates the reliability of the feature attribution by assessing their consistency with the predicted depth map. Experimental results demonstrate that Saliency Maps and Integrated Gradients have good performance in highlighting the most important input features for MDE lightweight and deep models, respectively. Furthermore, we show that Attribution Fidelity effectively identifies whether an explainability method fails to produce reliable visual maps, even in scenarios where conventional metrics might suggest satisfactory results.

