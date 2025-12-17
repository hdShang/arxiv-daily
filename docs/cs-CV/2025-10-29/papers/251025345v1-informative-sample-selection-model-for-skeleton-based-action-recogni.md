---
layout: default
title: Informative Sample Selection Model for Skeleton-based Action Recognition with Limited Training Samples
---

# Informative Sample Selection Model for Skeleton-based Action Recognition with Limited Training Samples

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.25345" target="_blank" class="toolbar-btn">arXiv: 2510.25345v1</a>
    <a href="https://arxiv.org/pdf/2510.25345.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25345v1" 
            onclick="toggleFavorite(this, '2510.25345v1', 'Informative Sample Selection Model for Skeleton-based Action Recognition with Limited Training Samples')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhigang Tu, Zhengbo Zhang, Jia Gong, Junsong Yuan, Bo Du

**分类**: cs.CV

**发布日期**: 2025-10-29

**备注**: Accepted by IEEE Transactions on Image Processing (TIP), 2025

---

## 💡 一句话要点

**提出基于MDP的骨骼动作识别信息样本选择模型，提升有限样本下的识别精度。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `骨骼动作识别` `半监督学习` `主动学习` `马尔可夫决策过程` `强化学习`

## 📋 核心要点

1. 现有主动学习方法选择代表性样本，但忽略了模型已学习的知识，导致信息冗余。
2. 论文将样本选择建模为MDP，训练智能体选择最具信息量的样本，提升模型学习效率。
3. 通过双曲空间投影增强状态表示，并引入元调优加速模型部署，实验验证了有效性。

## 📝 摘要（中文）

本文针对有限训练样本下的骨骼动作识别问题，即半监督3D动作识别，提出了一种新的信息样本选择模型。现有方法通常采用主动学习策略，通过编码器-解码器框架将骨骼序列嵌入到潜在空间，并结合聚类信息和基于margin的选择策略来选择最具信息量的未标注样本。然而，最具代表性的样本不一定最具信息量。为了解决这个问题，本文将半监督3D动作识别问题重新建模为一个马尔可夫决策过程（MDP），并训练一个信息样本选择模型来指导样本选择。为了增强状态-动作对中因素的表征能力，本文将其从欧几里得空间投影到双曲空间。此外，还引入了一种元调优策略来加速该方法在实际场景中的部署。在三个3D动作识别基准数据集上的大量实验表明了该方法的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决有限训练样本下，基于骨骼的3D动作识别问题。现有主动学习方法在选择用于标注的样本时，往往侧重于选择最具代表性的样本，而忽略了模型已经学习到的知识。这导致选择的样本可能包含冗余信息，降低了模型训练的效率，尤其是在标注成本高昂的情况下，如何高效地选择信息量大的样本至关重要。

**核心思路**：论文的核心思路是将半监督3D动作识别中的主动学习过程建模为一个马尔可夫决策过程（MDP）。通过训练一个智能体（Agent），使其能够根据当前模型的状态，选择最具信息量的样本进行标注，从而最大化模型性能的提升。这种方法能够动态地调整样本选择策略，避免选择冗余信息，提高学习效率。

**技术框架**：该方法的技术框架主要包含以下几个模块：1) 特征提取模块：用于提取骨骼序列的特征表示。2) MDP建模模块：将样本选择过程建模为MDP，定义状态、动作和奖励函数。状态表示当前模型的状态和未标注样本的信息，动作表示选择哪个样本进行标注，奖励函数反映了选择该样本后模型性能的提升。3) 智能体训练模块：使用强化学习算法训练智能体，使其能够学习到最优的样本选择策略。4) 双曲空间投影模块：将状态和动作从欧几里得空间投影到双曲空间，以增强其表征能力。5) 元调优模块：用于加速模型在实际场景中的部署。

**关键创新**：该方法最重要的技术创新点在于将主动学习过程建模为MDP，并使用强化学习算法训练智能体进行样本选择。与传统的主动学习方法相比，该方法能够动态地调整样本选择策略，避免选择冗余信息，提高学习效率。此外，使用双曲空间投影增强状态和动作的表征能力也是一个创新点。

**关键设计**：在MDP建模中，状态空间的设计需要充分考虑模型的状态和未标注样本的信息。奖励函数的设计需要能够准确地反映选择样本后模型性能的提升。在智能体训练中，可以选择合适的强化学习算法，如Q-learning或Policy Gradient等。双曲空间投影可以使用Poincaré ball模型或Hyperboloid模型。元调优可以使用Model-Agnostic Meta-Learning (MAML)等方法。

## 📊 实验亮点

该方法在三个3D动作识别基准数据集上进行了实验，结果表明该方法能够显著提高模型在有限标注数据下的识别精度。具体来说，与现有的主动学习方法相比，该方法在相同标注数据量下，能够取得更高的识别准确率，并且能够更快地达到相同的性能水平。实验结果验证了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要进行动作识别的场景，例如视频监控、人机交互、康复训练等。在这些场景中，标注数据往往是昂贵的，因此利用少量标注数据和大量未标注数据进行训练具有重要的实际价值。该方法可以提高模型在有限标注数据下的识别精度，降低标注成本，加速模型部署。

## 📄 摘要（原文）

> Skeleton-based human action recognition aims to classify human skeletal sequences, which are spatiotemporal representations of actions, into predefined categories. To reduce the reliance on costly annotations of skeletal sequences while maintaining competitive recognition accuracy, the task of 3D Action Recognition with Limited Training Samples, also known as semi-supervised 3D Action Recognition, has been proposed. In addition, active learning, which aims to proactively select the most informative unlabeled samples for annotation, has been explored in semi-supervised 3D Action Recognition for training sample selection. Specifically, researchers adopt an encoder-decoder framework to embed skeleton sequences into a latent space, where clustering information, combined with a margin-based selection strategy using a multi-head mechanism, is utilized to identify the most informative sequences in the unlabeled set for annotation. However, the most representative skeleton sequences may not necessarily be the most informative for the action recognizer, as the model may have already acquired similar knowledge from previously seen skeleton samples. To solve it, we reformulate Semi-supervised 3D action recognition via active learning from a novel perspective by casting it as a Markov Decision Process (MDP). Built upon the MDP framework and its training paradigm, we train an informative sample selection model to intelligently guide the selection of skeleton sequences for annotation. To enhance the representational capacity of the factors in the state-action pairs within our method, we project them from Euclidean space to hyperbolic space. Furthermore, we introduce a meta tuning strategy to accelerate the deployment of our method in real-world scenarios. Extensive experiments on three 3D action recognition benchmarks demonstrate the effectiveness of our method.

