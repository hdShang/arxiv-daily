---
layout: default
title: Dataset Distillation with Probabilistic Latent Features
---

# Dataset Distillation with Probabilistic Latent Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06647" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06647v2</a>
  <a href="https://arxiv.org/pdf/2505.06647.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06647v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06647v2', 'Dataset Distillation with Probabilistic Latent Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Li, Sarah Cechnicka, Cheng Ouyang, Katharina Breininger, Peter Schüffler, Bernhard Kainz

**分类**: cs.CV

**发布日期**: 2025-05-10 (更新: 2025-05-17)

**备注**: 23 pages

---

## 💡 一句话要点

**提出基于概率潜在特征的数据集蒸馏方法以降低计算成本**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数据集蒸馏` `深度学习` `合成数据` `概率模型` `计算机视觉` `模型训练`

## 📋 核心要点

1. 现有的数据集蒸馏方法通常依赖于将数据从像素空间映射到潜在空间，难以有效捕捉数据的空间结构。
2. 本文提出了一种基于概率潜在特征的随机方法，通过建模潜在特征的联合分布来生成合成数据。
3. 在多个基准数据集上进行验证后，提出的方法在多种骨干网络上实现了最先进的性能，显示出其有效性。

## 📝 摘要（中文）

随着深度学习模型的复杂性增加和训练数据量的扩大，降低存储和计算成本变得愈发重要。数据集蒸馏通过合成一组紧凑的合成数据，有效替代原始数据集。现有方法通常依赖于将数据从像素空间映射到生成模型的潜在空间，而本文提出了一种新的随机方法，建模潜在特征的联合分布。这种方法能够更好地捕捉空间结构，生成多样化的合成样本，从而有利于模型训练。我们引入了一种由轻量网络参数化的低秩多元正态分布，保持了低计算复杂度，并兼容多种用于数据集蒸馏的匹配网络。经过蒸馏后，通过将学习到的潜在特征输入预训练生成器生成合成图像，并用于训练分类模型，最终在真实测试集上进行评估。我们在多个基准数据集上验证了该方法，包括ImageNet子集、CIFAR-10和MedMNIST组织病理数据集，结果显示其在多种骨干网络上实现了最先进的跨架构性能，证明了其通用性和有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数据集蒸馏方法在捕捉数据空间结构方面的不足，尤其是在生成合成数据时的多样性和有效性问题。

**核心思路**：我们提出了一种新的随机方法，通过建模潜在特征的联合分布来生成合成数据。这种方法能够更好地捕捉数据的空间结构，进而提高模型训练的效果。

**技术框架**：整体架构包括三个主要模块：首先，使用轻量网络参数化的低秩多元正态分布来学习潜在特征；其次，将学习到的潜在特征输入到预训练生成器中生成合成图像；最后，利用这些合成图像训练分类模型并进行性能评估。

**关键创新**：本文的主要创新在于引入了一种新的概率模型来描述潜在特征的联合分布，这与传统方法的像素空间映射形成了本质区别，使得生成的合成样本更加多样化。

**关键设计**：在参数设置上，我们采用了轻量级网络以保持低计算复杂度，损失函数设计上则考虑了生成样本的多样性和质量，确保生成的合成数据能够有效替代原始数据集。

## 📊 实验亮点

在多个基准数据集上进行的实验表明，提出的方法在多种骨干网络上实现了最先进的性能，特别是在ImageNet子集和CIFAR-10上，性能提升幅度超过了现有最优方法，展示了其优越性和广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、医疗影像分析和自动驾驶等领域，能够有效降低数据存储和处理成本，同时提高模型的训练效率。未来，该方法有望在大规模数据集的处理和模型训练中发挥重要作用，推动相关领域的发展。

## 📄 摘要（原文）

> As deep learning models grow in complexity and the volume of training data increases, reducing storage and computational costs becomes increasingly important. Dataset distillation addresses this challenge by synthesizing a compact set of synthetic data that can effectively replace the original dataset in downstream classification tasks. While existing methods typically rely on mapping data from pixel space to the latent space of a generative model, we propose a novel stochastic approach that models the joint distribution of latent features. This allows our method to better capture spatial structures and produce diverse synthetic samples, which benefits model training. Specifically, we introduce a low-rank multivariate normal distribution parameterized by a lightweight network. This design maintains low computational complexity and is compatible with various matching networks used in dataset distillation. After distillation, synthetic images are generated by feeding the learned latent features into a pretrained generator. These synthetic images are then used to train classification models, and performance is evaluated on real test set. We validate our method on several benchmarks, including ImageNet subsets, CIFAR-10, and the MedMNIST histopathological dataset. Our approach achieves state-of-the-art cross architecture performance across a range of backbone architectures, demonstrating its generality and effectiveness.

