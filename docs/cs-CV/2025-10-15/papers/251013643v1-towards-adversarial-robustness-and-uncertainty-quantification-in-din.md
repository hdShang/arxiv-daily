---
layout: default
title: Towards Adversarial Robustness and Uncertainty Quantification in DINOv2-based Few-Shot Anomaly Detection
---

# Towards Adversarial Robustness and Uncertainty Quantification in DINOv2-based Few-Shot Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13643" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13643v1</a>
  <a href="https://arxiv.org/pdf/2510.13643.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13643v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13643v1', 'Towards Adversarial Robustness and Uncertainty Quantification in DINOv2-based Few-Shot Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akib Mohammed Khan, Bartosz Krawczyk

**分类**: cs.CV

**发布日期**: 2025-10-15

**备注**: 10 pages, 5 figures, 3 tables

---

## 💡 一句话要点

**研究DINOv2在少样本异常检测中的对抗鲁棒性和不确定性量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `异常检测` `对抗鲁棒性` `不确定性量化` `DINOv2` `对抗攻击` `Platt缩放`

## 📋 核心要点

1. 现有基于DINOv2的少样本异常检测方法缺乏对抗鲁棒性分析，易受对抗攻击影响，且异常分数的不确定性未被有效量化。
2. 本文提出一种评估和提升DINOv2异常检测器对抗鲁棒性和不确定性量化的方法，通过附加线性头进行对抗攻击，并使用Platt缩放进行校准。
3. 实验表明，DINOv2异常检测器易受对抗攻击，且原始异常分数校准不良。通过Platt缩放校准后，可有效提高对抗样本的检测能力。

## 📝 摘要（中文）

DINOv2等基础模型在少样本异常检测中表现出色，但其对抗扰动的敏感性和异常分数的校准不确定性仍未得到充分研究。本文基于AnomalyDINO（一种基于DINOv2特征的无训练深度近邻检测器），首次系统性地研究了该场景下的对抗攻击和不确定性估计。为了在保持测试时行为的同时实现白盒梯度攻击，我们仅在冻结的DINOv2特征上附加了一个轻量级线性头来生成扰动。通过在MVTec-AD和VisA数据集上评估FGSM的影响，我们观察到F1、AUROC、AP和G-mean的一致下降，表明微小的扰动会翻转特征空间中的近邻关系，从而导致置信的错误分类。此外，我们发现原始异常分数校准不良，揭示了置信度和正确性之间的差距，限制了其在安全关键型应用中的使用。作为提高可信度的一种简单而有效的基线方法，我们应用事后Platt缩放来校准异常分数，以进行不确定性估计。由此产生的校准后验概率在对抗扰动输入上的预测熵明显高于干净输入，从而实现了一种实用的攻击检测标记机制，同时降低了校准误差（ECE）。我们的研究结果揭示了基于DINOv2的少样本异常检测器的具体漏洞，并建立了一个评估协议和基线，用于实现鲁棒的、具有不确定性意识的异常检测。我们认为，对抗鲁棒性和有原则的不确定性量化不是可选项，而是异常检测系统要实现可信赖和为实际部署做好准备的必要能力。

## 🔬 方法详解

**问题定义**：论文旨在解决基于DINOv2的少样本异常检测器在面对对抗攻击时的脆弱性问题，以及其输出的异常分数缺乏良好校准的问题。现有方法未能充分考虑对抗扰动对特征空间的影响，并且原始异常分数无法提供可靠的不确定性估计，限制了其在安全关键领域的应用。

**核心思路**：论文的核心思路是通过引入对抗攻击来评估DINOv2异常检测器的鲁棒性，并利用Platt缩放等方法来校准异常分数，从而提高其不确定性估计的准确性。通过对抗攻击，可以暴露模型在面对恶意输入时的弱点；通过校准，可以使异常分数更好地反映模型预测的置信度。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 使用预训练的DINOv2模型提取图像特征；2) 基于提取的特征，使用AnomalyDINO构建无训练的近邻异常检测器；3) 为了进行白盒攻击，附加一个轻量级的线性头到冻结的DINOv2特征上，用于生成对抗扰动；4) 使用FGSM等方法生成对抗样本，并评估其对异常检测性能的影响；5) 使用Platt缩放等方法对异常分数进行校准，并评估校准后的不确定性估计效果。

**关键创新**：论文的关键创新在于：1) 首次系统性地研究了基于DINOv2的少样本异常检测器在对抗攻击下的鲁棒性；2) 提出了一种简单有效的对抗攻击方法，通过附加线性头来生成扰动，同时保持测试时行为；3) 探索了使用Platt缩放等方法来校准异常分数，从而提高不确定性估计的准确性。

**关键设计**：论文的关键设计包括：1) 使用轻量级线性头进行对抗攻击，避免修改预训练的DINOv2模型；2) 使用FGSM算法生成对抗样本，并调整扰动幅度以评估鲁棒性；3) 使用Platt缩放对异常分数进行校准，并使用ECE等指标评估校准效果；4) 使用预测熵来评估对抗样本的不确定性。

## 📊 实验亮点

实验结果表明，基于DINOv2的异常检测器易受FGSM攻击，F1、AUROC、AP和G-mean等指标均显著下降。通过Platt缩放校准后，对抗样本的预测熵显著高于干净样本，ECE指标也得到降低，表明校准后的异常分数能够更准确地反映模型的不确定性。

## 🎯 应用场景

该研究成果可应用于工业异常检测、医疗图像分析、自动驾驶安全等领域。通过提高异常检测系统的对抗鲁棒性和不确定性量化能力，可以增强其在实际部署中的可靠性和安全性，减少误报和漏报，从而降低潜在风险。

## 📄 摘要（原文）

> Foundation models such as DINOv2 have shown strong performance in few-shot anomaly detection, yet two key questions remain unexamined: (i) how susceptible are these detectors to adversarial perturbations; and (ii) how well do their anomaly scores reflect calibrated uncertainty? Building on AnomalyDINO, a training-free deep nearest-neighbor detector over DINOv2 features, we present one of the first systematic studies of adversarial attacks and uncertainty estimation in this setting. To enable white-box gradient attacks while preserving test-time behavior, we attach a lightweight linear head to frozen DINOv2 features only for crafting perturbations. Using this heuristic, we evaluate the impact of FGSM across the MVTec-AD and VisA datasets and observe consistent drops in F1, AUROC, AP, and G-mean, indicating that imperceptible perturbations can flip nearest-neighbor relations in feature space to induce confident misclassification. Complementing robustness, we probe reliability and find that raw anomaly scores are poorly calibrated, revealing a gap between confidence and correctness that limits safety-critical use. As a simple, strong baseline toward trustworthiness, we apply post-hoc Platt scaling to the anomaly scores for uncertainty estimation. The resulting calibrated posteriors yield significantly higher predictive entropy on adversarially perturbed inputs than on clean ones, enabling a practical flagging mechanism for attack detection while reducing calibration error (ECE). Our findings surface concrete vulnerabilities in DINOv2-based few-shot anomaly detectors and establish an evaluation protocol and baseline for robust, uncertainty-aware anomaly detection. We argue that adversarial robustness and principled uncertainty quantification are not optional add-ons but essential capabilities if anomaly detection systems are to be trustworthy and ready for real-world deployment.

