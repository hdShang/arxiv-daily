---
layout: default
title: "Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls"
---

# Why Can't Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00184" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00184v1</a>
  <a href="https://arxiv.org/pdf/2510.00184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00184v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00184v1', 'Why Can\'t Transformers Learn Multiplication? Reverse-Engineering Reveals Long-Range Dependency Pitfalls')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyan Bai, Itamar Pres, Yuntian Deng, Chenhao Tan, Stuart Shieber, Fernanda Viégas, Martin Wattenberg, Andrew Lee

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**Transformer无法学习乘法？逆向工程揭示了长程依赖的陷阱**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Transformer` `长程依赖` `逆向工程` `归纳偏置` `注意力机制`

## 📋 核心要点

1. 现有Transformer模型在多位数乘法等需要长程依赖的任务上表现不佳，暴露了其在处理复杂逻辑推理上的局限性。
2. 通过逆向工程一个成功的乘法模型，发现其利用注意力机制构建有向无环图来缓存和检索部分乘积，从而实现长程依赖。
3. 引入预测“运行总和”的辅助损失，为模型提供归纳偏置，成功提升了Transformer在多位数乘法任务上的性能。

## 📝 摘要（中文）

语言模型的能力日益增强，但仍然无法完成看似简单的多位数乘法任务。本文通过逆向工程一个成功学习乘法的模型（通过隐式思维链），研究了其原因，并报告了三个发现：（1）长程结构的证据：Logit归因和线性探针表明，该模型编码了多位数乘法所需的必要长程依赖。（2）机制：该模型使用注意力机制构建有向无环图来“缓存”和“检索”成对的部分乘积，从而编码长程依赖。（3）几何：该模型通过在数字对之间形成闵可夫斯基和，在注意力头中实现部分乘积，并且数字使用傅里叶基表示，这两种表示方法都是标准微调模型所缺乏的直观且有效的表示方法。基于这些见解，我们重新审视了标准微调的学习动态，发现该模型收敛到缺乏所需长程依赖的局部最优解。我们通过引入一个辅助损失来预测“运行总和”（通过线性回归探针）来进一步验证这种理解，该辅助损失提供了一种归纳偏置，使模型能够成功学习多位数乘法。总之，通过逆向工程隐式思维链模型的机制，我们揭示了Transformer学习长程依赖的一个陷阱，并提供了一个正确的归纳偏置如何解决此问题的例子。

## 🔬 方法详解

**问题定义**：论文旨在解决Transformer模型在学习多位数乘法时遇到的困难。现有的Transformer模型在处理需要长程依赖的任务时表现不佳，无法有效地捕捉数字之间的复杂关系，导致乘法运算的准确率较低。这种失败表明Transformer在某些类型的推理任务中存在固有的局限性。

**核心思路**：论文的核心思路是通过逆向工程一个能够成功学习乘法的Transformer模型，来理解其内部机制，并找出标准Transformer模型失败的原因。通过分析成功模型的结构、表示方法和学习动态，揭示其如何有效地编码和利用长程依赖关系。然后，将这些见解应用于改进标准Transformer模型的训练过程。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 训练一个能够成功学习乘法的Transformer模型（通过隐式思维链）。2) 使用logit归因和线性探针等技术，分析该模型的内部表示和注意力机制，揭示其如何编码长程依赖。3) 研究该模型中数字的表示方式（傅里叶基）以及部分乘积的实现方式（闵可夫斯基和）。4) 分析标准Transformer模型的学习动态，找出其收敛到局部最优解的原因。5) 引入辅助损失（预测运行总和）来提供归纳偏置，并验证其对提升模型性能的有效性。

**关键创新**：论文最重要的技术创新点在于通过逆向工程揭示了Transformer模型学习长程依赖的陷阱，并提出了通过引入辅助损失来提供归纳偏置的解决方案。具体来说，发现成功模型使用注意力机制构建有向无环图来缓存和检索部分乘积，以及使用傅里叶基表示数字和闵可夫斯基和实现部分乘积，是标准模型所缺乏的关键要素。

**关键设计**：论文的关键设计包括：1) 使用注意力机制构建有向无环图来表示部分乘积之间的依赖关系。2) 使用傅里叶基来表示数字，这使得模型能够更有效地学习数字之间的关系。3) 引入预测“运行总和”的辅助损失，通过线性回归探针实现，为模型提供关于乘法运算过程的归纳偏置。这个辅助损失鼓励模型学习中间步骤，从而更容易捕捉长程依赖。

## 📊 实验亮点

论文通过实验证明，标准Transformer模型在多位数乘法任务上表现不佳，而通过逆向工程得到的模型能够成功学习乘法。引入预测“运行总和”的辅助损失后，标准模型的性能得到了显著提升，验证了长程依赖和归纳偏置的重要性。具体性能数据未知，但该方法为解决Transformer在长程依赖任务中的问题提供了一种有效途径。

## 🎯 应用场景

该研究的潜在应用领域包括提升语言模型在需要复杂推理和计算的任务中的表现，例如科学计算、金融建模和代码生成。通过理解和解决Transformer模型在长程依赖学习方面的局限性，可以开发更强大的AI系统，更好地处理现实世界中的复杂问题。此外，该研究也为设计更有效的神经网络架构和训练方法提供了新的思路。

## 📄 摘要（原文）

> Language models are increasingly capable, yet still fail at a seemingly simple task of multi-digit multiplication. In this work, we study why, by reverse-engineering a model that successfully learns multiplication via \emph{implicit chain-of-thought}, and report three findings: (1) Evidence of long-range structure: Logit attributions and linear probes indicate that the model encodes the necessary long-range dependencies for multi-digit multiplication. (2) Mechanism: the model encodes long-range dependencies using attention to construct a directed acyclic graph to ``cache'' and ``retrieve'' pairwise partial products. (3) Geometry: the model implements partial products in attention heads by forming Minkowski sums between pairs of digits, and digits are represented using a Fourier basis, both of which are intuitive and efficient representations that the standard fine-tuning model lacks. With these insights, we revisit the learning dynamics of standard fine-tuning and find that the model converges to a local optimum that lacks the required long-range dependencies. We further validate this understanding by introducing an auxiliary loss that predicts the ``running sum'' via a linear regression probe, which provides an inductive bias that enables the model to successfully learn multi-digit multiplication. In summary, by reverse-engineering the mechanisms of an implicit chain-of-thought model we uncover a pitfall for learning long-range dependencies in Transformers and provide an example of how the correct inductive bias can address this issue.

