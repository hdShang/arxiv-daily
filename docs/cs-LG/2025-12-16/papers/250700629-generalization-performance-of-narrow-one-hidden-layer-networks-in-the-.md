---
layout: default
title: Generalization performance of narrow one-hidden layer networks in the teacher-student setting
---

# Generalization performance of narrow one-hidden layer networks in the teacher-student setting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00629" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00629</a>
  <a href="https://arxiv.org/pdf/2507.00629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00629" onclick="toggleFavorite(this, '2507.00629', 'Generalization performance of narrow one-hidden layer networks in the teacher-student setting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jean Barbier, Federica Gerace, Alessandro Ingrosso, Clarissa Lauditi, Enrico M. Malatesta, Gibbs Nwemadji, Rodrigo Pérez Ortiz

**分类**: cs.LG, math.PR, math.ST

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对窄单隐层网络，提出基于师生框架的泛化性能理论分析方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `神经网络泛化` `师生框架` `统计物理` `窄网络` `单隐层网络`

## 📋 核心要点

1. 现有方法缺乏对具有通用激活函数的全连接单隐层网络泛化性能的完整理论描述，尤其是在窄网络的情况下。
2. 该论文利用统计物理学的方法，为窄网络的泛化性能提供了闭式表达式，并揭示了隐藏神经元专业化转变的现象。
3. 实验结果表明，该理论能够准确预测神经网络在回归或分类任务中的泛化误差，验证了理论的有效性。

## 📝 摘要（中文）

理解神经网络在简单输入输出分布下的泛化能力，对于解释其在真实数据集上的学习性能至关重要。经典的师生框架提供了一个完美的理论测试平台，其中学生网络从由教师模型生成的数据中学习。然而，目前缺乏对具有通用激活函数的全连接单隐层网络性能的完整理论描述。本文针对窄网络（即隐藏单元数量远小于输入维度）提出了这样的通用理论。利用统计物理学的方法，我们为有限温度（贝叶斯）和经验风险最小化估计器的典型性能提供了闭式表达式，这些表达式仅依赖于少量的统计量。我们强调，当样本数量足够大且与网络参数数量成比例时，隐藏神经元会发生专业化转变。我们的理论能够准确预测神经网络在回归或分类任务中使用噪声全批量梯度下降（朗之万动力学）或全批量梯度下降训练时的泛化误差。

## 🔬 方法详解

**问题定义**：该论文旨在解决窄单隐层神经网络在师生框架下的泛化性能分析问题。现有方法缺乏对具有通用激活函数的全连接单隐层网络性能的完整理论描述，尤其是在隐藏单元数量远小于输入维度的情况下，难以准确预测网络的泛化误差。

**核心思路**：论文的核心思路是利用统计物理学中的方法，对窄网络的泛化性能进行理论分析。通过将神经网络的学习过程类比于物理系统，可以推导出泛化误差的闭式表达式，从而更好地理解网络的学习行为。这种方法能够捕捉到网络中的一些关键现象，例如隐藏神经元的专业化转变。

**技术框架**：该论文的技术框架主要包括以下几个步骤：1) 建立师生框架下的窄单隐层神经网络模型；2) 利用统计物理学中的副本方法或腔方法，计算网络的自由能或配分函数；3) 从自由能或配分函数中推导出泛化误差的闭式表达式；4) 通过实验验证理论预测的准确性。

**关键创新**：该论文的关键创新在于：1) 提出了针对窄单隐层网络的泛化性能的完整理论分析方法；2) 利用统计物理学的方法，推导出了泛化误差的闭式表达式，为理解网络的学习行为提供了新的视角；3) 揭示了隐藏神经元专业化转变的现象，并分析了其对泛化性能的影响。

**关键设计**：论文中关键的设计包括：1) 假设隐藏单元的数量远小于输入维度，从而简化了理论分析；2) 使用通用激活函数，使得理论分析具有更广泛的适用性；3) 考虑了有限温度（贝叶斯）和经验风险最小化两种不同的学习方式；4) 通过噪声全批量梯度下降（朗之万动力学）或全批量梯度下降进行训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.00629/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.00629/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.00629/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文通过实验验证了理论预测的准确性。实验结果表明，该理论能够准确预测神经网络在回归或分类任务中使用噪声全批量梯度下降（朗之万动力学）或全批量梯度下降训练时的泛化误差。此外，实验还验证了隐藏神经元专业化转变现象的存在，并分析了其对泛化性能的影响。具体的性能数据和对比基线在论文中进行了详细的展示。

## 🎯 应用场景

该研究成果可应用于理解和优化神经网络的训练过程，特别是在资源受限的场景下。通过理论分析，可以更好地选择合适的网络结构和训练参数，提高模型的泛化能力。此外，该研究还可以为设计更高效的神经网络架构提供理论指导，例如，通过控制隐藏神经元的专业化程度来提高模型的性能。

## 📄 摘要（原文）

> Understanding the generalization abilities of neural networks for simple input-output distributions is crucial to account for their learning performance on real datasets. The classical teacher-student setting, where a network is trained from data obtained thanks to a label-generating teacher model, serves as a perfect theoretical test bed. In this context, a complete theoretical account of the performance of fully connected one-hidden layer networks in the presence of generic activation functions is lacking. In this work, we develop such a general theory for narrow networks, i.e. with a large number of hidden units, yet much smaller than the input dimension. Using methods from statistical physics, we provide closed-form expressions for the typical performance of both finite temperature (Bayesian) and empirical risk minimization estimators, in terms of a small number of summary statistics. In doing so, we highlight the presence of a transition where hidden neurons specialize when the number of samples is sufficiently large and proportional to the number of parameters of the network. Our theory accurately predicts the generalization error of neural networks trained on regression or classification tasks with either noisy full-batch gradient descent (Langevin dynamics) or full-batch gradient descent.

