---
layout: default
title: "The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain"
---

# The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26507" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26507v1</a>
  <a href="https://arxiv.org/pdf/2509.26507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26507v1', 'The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adrian Kosowski, Przemysław Uznański, Jan Chorowski, Zuzanna Stamirowska, Michał Bartoszkiewicz

**分类**: cs.NE, cs.AI, cs.LG, stat.ML

**发布日期**: 2025-09-30

**备注**: Code available at: https://github.com/pathwaycom/bdh Accompanying blog: https://pathway.com/research/bdh

---

## 💡 一句话要点

**提出Dragon Hatchling：一种受生物启发的、可解释的类Transformer语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生物启发神经网络` `可解释性AI` `大型语言模型` `赫布学习` `脉冲神经元`

## 📋 核心要点

1. 现有机器学习模型在通用推理方面存在瓶颈，难以像大脑一样进行时间泛化。
2. Dragon Hatchling (BDH) 是一种基于生物启发网络的语言模型，旨在实现 Transformer 级别的性能，同时提供内在的可解释性。
3. 实验表明，BDH 在语言和翻译任务上与 GPT2 性能相当，且具有生物合理性和可解释性。

## 📝 摘要（中文）

本文介绍了一种新的大型语言模型架构“Dragon Hatchling”(BDH)，它基于一个具有尺度不变性的、受生物学启发的神经元粒子网络，这些粒子进行局部交互。BDH结合了强大的理论基础和内在的可解释性，同时不牺牲类似Transformer的性能。BDH是一种实用的、高性能的、基于注意力机制的状态空间序列学习架构。除了作为一个图模型，BDH还具有GPU友好的公式。它表现出类似Transformer的缩放规律：经验表明，对于相同的训练数据，在相同数量的参数（1000万到10亿）下，BDH在语言和翻译任务上与GPT2的性能相当。BDH可以被表示为一个大脑模型。BDH在推理过程中的工作记忆完全依赖于具有赫布学习的突触可塑性，使用脉冲神经元。经验证实，当BDH在处理语言输入时听到或推理关于特定概念时，特定的、单独的突触会加强连接。BDH的神经元交互网络是一个具有高模块化和重尾度分布的图。BDH模型在生物学上是合理的，解释了人类神经元可能使用的一种实现语音的机制。BDH专为可解释性而设计。BDH的激活向量是稀疏且正的。我们在语言任务中展示了BDH的单义性。状态的可解释性，超越了神经元和模型参数的可解释性，是BDH架构的固有特征。

## 🔬 方法详解

**问题定义**：现有的大型语言模型虽然在各种任务上取得了显著的成果，但在可解释性和生物合理性方面存在不足。此外，它们在处理时间序列数据时，难以像生物大脑一样进行泛化。因此，需要一种既能保持高性能，又能提供内在可解释性，并且更接近生物神经机制的模型。

**核心思路**：Dragon Hatchling (BDH) 的核心思路是构建一个基于尺度不变的、受生物学启发的神经元粒子网络。该网络中的神经元进行局部交互，并通过赫布学习进行突触可塑性调整。这种设计旨在模拟大脑的工作方式，从而提高模型的可解释性和泛化能力。

**技术框架**：BDH 的整体架构是一个基于注意力机制的状态空间序列学习模型。它由多个神经元粒子组成，这些粒子通过图结构连接。模型包含以下主要模块：输入嵌入层、神经元交互层、输出层。神经元交互层是 BDH 的核心，负责模拟神经元之间的局部交互和突触可塑性。

**关键创新**：BDH 的关键创新在于其基于生物启发的神经元交互网络和赫布学习机制。与传统的 Transformer 模型不同，BDH 的神经元之间的连接不是完全连接的，而是通过一个具有尺度不变性的图结构连接。此外，BDH 使用赫布学习来调整神经元之间的连接强度，从而实现工作记忆和概念学习。

**关键设计**：BDH 的关键设计包括：1) 使用脉冲神经元来模拟生物神经元的激活机制；2) 使用稀疏且正的激活向量来提高模型的可解释性；3) 使用具有高模块化和重尾度分布的图结构来连接神经元；4) 使用赫布学习规则来调整神经元之间的连接强度。损失函数的设计目标是最小化预测误差，并鼓励神经元之间的稀疏连接。

## 📊 实验亮点

实验结果表明，BDH 在语言和翻译任务上与 GPT2 具有相当的性能，同时具有更高的可解释性。具体来说，在相同的参数规模和训练数据下，BDH 能够达到与 GPT2 相似的准确率。此外，实验还证实了 BDH 的神经元交互网络具有高模块化和重尾度分布，并且特定的突触会在模型处理特定概念时加强连接。

## 🎯 应用场景

BDH 模型具有广泛的应用前景，包括自然语言处理、机器翻译、语音识别等领域。由于其内在的可解释性，BDH 还可以应用于医疗诊断、金融风险评估等需要高度透明度的领域。此外，BDH 的生物合理性使其成为研究大脑工作机制的有力工具，有助于推动神经科学的发展。

## 📄 摘要（原文）

> The relationship between computing systems and the brain has served as motivation for pioneering theoreticians since John von Neumann and Alan Turing. Uniform, scale-free biological networks, such as the brain, have powerful properties, including generalizing over time, which is the main barrier for Machine Learning on the path to Universal Reasoning Models.
>   We introduce `Dragon Hatchling' (BDH), a new Large Language Model architecture based on a scale-free biologically inspired network of \$n\$ locally-interacting neuron particles. BDH couples strong theoretical foundations and inherent interpretability without sacrificing Transformer-like performance.
>   BDH is a practical, performant state-of-the-art attention-based state space sequence learning architecture. In addition to being a graph model, BDH admits a GPU-friendly formulation. It exhibits Transformer-like scaling laws: empirically BDH rivals GPT2 performance on language and translation tasks, at the same number of parameters (10M to 1B), for the same training data.
>   BDH can be represented as a brain model. The working memory of BDH during inference entirely relies on synaptic plasticity with Hebbian learning using spiking neurons. We confirm empirically that specific, individual synapses strengthen connection whenever BDH hears or reasons about a specific concept while processing language inputs. The neuron interaction network of BDH is a graph of high modularity with heavy-tailed degree distribution. The BDH model is biologically plausible, explaining one possible mechanism which human neurons could use to achieve speech.
>   BDH is designed for interpretability. Activation vectors of BDH are sparse and positive. We demonstrate monosemanticity in BDH on language tasks. Interpretability of state, which goes beyond interpretability of neurons and model parameters, is an inherent feature of the BDH architecture.

