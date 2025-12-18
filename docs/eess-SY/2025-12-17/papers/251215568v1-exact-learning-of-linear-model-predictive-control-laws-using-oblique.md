---
layout: default
title: Exact Learning of Linear Model Predictive Control Laws using Oblique Decision Trees with Linear Predictions
---

# Exact Learning of Linear Model Predictive Control Laws using Oblique Decision Trees with Linear Predictions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15568" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15568v1</a>
  <a href="https://arxiv.org/pdf/2512.15568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15568v1" onclick="toggleFavorite(this, '2512.15568v1', 'Exact Learning of Linear Model Predictive Control Laws using Oblique Decision Trees with Linear Predictions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayang Ren, Qiangqiang Mao, Tianwei Zhao, Yankai Cao

**分类**: math.OC, eess.SY

**发布日期**: 2025-12-17

**备注**: 6 pages, 4 figures, accepted by and presented at the 64th IEEE Conference on Decision and Control (CDC) in December 2025

---

## 💡 一句话要点

**提出基于斜决策树的线性模型预测控制法以提升计算效率与可解释性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `斜决策树` `线性预测` `实时控制` `安全关键系统` `计算效率` `可解释性`

## 📋 核心要点

1. 现有的模型预测控制方法在实时应用中面临计算复杂性和可扩展性问题，限制了其在安全关键领域的应用。
2. 本文提出了一种新的数据驱动框架，利用斜决策树与线性预测直接学习线性MPC控制律，兼顾计算效率与可解释性。
3. 实验结果显示，ODT-LP控制器在闭环性能上与传统MPC相当，但在线评估时间显著降低，提升幅度达到几个数量级。

## 📝 摘要（中文）

模型预测控制（MPC）是一种强大的多变量系统控制策略，但由于在线优化的需求，在实时部署中面临计算挑战。尽管显式MPC和神经网络近似方法缓解了这一负担，但它们在可扩展性或可解释性方面存在不足，限制了在安全关键系统中的应用。本文提出了一种数据驱动框架，直接从采样的状态-动作对中学习线性MPC控制律，采用斜决策树与线性预测（ODT-LP），实现了计算效率和可解释性的双重提升。通过利用线性MPC的分段仿射结构，证明了线性MPC控制律可以被有限深度的ODT-LP模型复制。我们开发了一种基于梯度的训练算法，使用平滑的树路由函数近似，从网格采样的线性MPC解中学习该结构，实现端到端优化。在有界近似误差下建立输入到状态的稳定性，并将误差分解为学习不准确性和采样误差，以指导模型设计。数值实验表明，ODT-LP控制器在闭环性能上与MPC相匹配，同时在线评估时间比MPC、显式MPC、神经网络和随机森林等方法减少了几个数量级。

## 🔬 方法详解

**问题定义**：本文旨在解决模型预测控制（MPC）在实时部署中的计算复杂性和可扩展性问题。现有的显式MPC和神经网络近似方法在可解释性和性能上存在不足，限制了其在安全关键系统中的应用。

**核心思路**：论文提出通过斜决策树与线性预测（ODT-LP）直接从状态-动作对中学习线性MPC控制律，利用其分段仿射结构实现高效且可解释的控制策略。

**技术框架**：整体架构包括数据采样、模型训练和控制律生成三个主要模块。首先，通过网格采样获取线性MPC解，然后使用梯度优化算法训练ODT-LP模型，最后生成控制律以实现实时控制。

**关键创新**：最重要的技术创新在于证明了线性MPC控制律可以通过有限深度的ODT-LP模型进行精确复制，且在有界近似误差下建立了输入到状态的稳定性。

**关键设计**：采用平滑的树路由函数近似作为损失函数，优化过程中关注学习不准确性和采样误差的分解，以指导模型设计和参数设置。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15568v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15568v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15568v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ODT-LP控制器在闭环性能上与传统MPC相当，同时在线评估时间显著降低，具体提升幅度达到几个数量级，展示了其在实时控制中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人控制和工业自动化等安全关键系统。通过提高控制策略的计算效率和可解释性，能够在实时环境中实现更可靠的决策支持，促进智能系统的广泛应用。

## 📄 摘要（原文）

> Model Predictive Control (MPC) is a powerful strategy for constrained multivariable systems but faces computational challenges in real-time deployment due to its online optimization requirements. While explicit MPC and neural network approximations mitigate this burden, they suffer from scalability issues or lack interpretability, limiting their applicability in safety-critical systems. This work introduces a data-driven framework that directly learns the Linear MPC control law from sampled state-action pairs using Oblique Decision Trees with Linear Predictions (ODT-LP), achieving both computational efficiency and interpretability. By leveraging the piecewise affine structure of Linear MPC, we prove that the Linear MPC control law can be replicated by finite-depth ODT-LP models. We develop a gradient-based training algorithm using smooth approximations of tree routing functions to learn this structure from grid-sampled Linear MPC solutions, enabling end-to-end optimization. Input-to-state stability is established under bounded approximation errors, with explicit error decomposition into learning inaccuracies and sampling errors to inform model design. Numerical experiments demonstrate that ODT-LP controllers match MPC's closed-loop performance while reducing online evaluation time by orders of magnitude compared to MPC, explicit MPC, neural network, and random forest counterparts. The transparent tree structure enables formal verification of control logic, bridging the gap between computational efficiency and certifiable reliability for safety-critical systems.

