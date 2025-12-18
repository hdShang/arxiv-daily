---
layout: default
title: A Dynamic Knowledge Distillation Method Based on the Gompertz Curve
---

# A Dynamic Knowledge Distillation Method Based on the Gompertz Curve

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21649" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21649v1</a>
  <a href="https://arxiv.org/pdf/2510.21649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21649v1', 'A Dynamic Knowledge Distillation Method Based on the Gompertz Curve')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Yang, Guangjun Qin

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-24

**备注**: 15 pages, 2 figures

---

## 💡 一句话要点

**提出Gompertz-CNN，利用Gompertz曲线动态调整知识蒸馏，提升学生模型性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `Gompertz曲线` `动态权重调整` `模型压缩` `深度学习` `Wasserstein距离` `梯度匹配`

## 📋 核心要点

1. 传统知识蒸馏方法忽略了学生模型学习能力随训练阶段的变化，导致知识传递效率降低。
2. Gompertz-CNN利用Gompertz曲线动态调整蒸馏损失权重，使知识传递与学生模型的学习阶段相匹配。
3. 实验结果表明，Gompertz-CNN在CIFAR-10和CIFAR-100数据集上显著优于传统方法，准确率分别提升高达8%和4%。

## 📝 摘要（中文）

本文提出了一种新的动态知识蒸馏框架Gompertz-CNN，该框架将Gompertz增长模型融入训练过程，以解决传统知识蒸馏的局限性。传统方法通常无法捕捉学生模型不断发展的认知能力，导致次优的知识转移。为了克服这一点，我们提出了一种阶段感知的蒸馏策略，该策略基于Gompertz曲线动态调整蒸馏损失的权重，反映了学生的学习过程：初始阶段缓慢增长，中期快速改进，以及后期饱和。我们的框架结合了Wasserstein距离来衡量特征层面的差异，并结合梯度匹配来对齐教师和学生模型之间的反向传播行为。这些组件统一在一个多损失目标下，其中Gompertz曲线调节蒸馏损失随时间的影响。在CIFAR-10和CIFAR-100上使用各种教师-学生架构（例如，ResNet50和MobileNet_v2）进行的大量实验表明，Gompertz-CNN始终优于传统的蒸馏方法，在CIFAR-10和CIFAR-100上分别实现了高达8%和4%的准确率提升。

## 🔬 方法详解

**问题定义**：传统知识蒸馏方法通常采用固定的损失权重，无法适应学生模型在不同训练阶段的学习能力变化。学生模型在训练初期学习能力较弱，后期逐渐饱和，固定的蒸馏损失权重可能导致欠拟合或过拟合，影响知识传递的效率和最终性能。

**核心思路**：本文的核心思路是利用Gompertz增长模型来模拟学生模型的学习过程，并基于Gompertz曲线动态调整蒸馏损失的权重。Gompertz曲线能够很好地描述学习过程中的S型增长模式，即初始阶段缓慢增长，中期快速增长，后期逐渐饱和。通过将蒸馏损失的权重与Gompertz曲线相结合，可以使知识传递更加符合学生模型的学习规律，从而提高知识传递的效率和最终性能。

**技术框架**：Gompertz-CNN框架主要包含以下几个模块：1) 教师模型和学生模型；2) 基于Gompertz曲线的动态权重调整模块；3) 特征层面的Wasserstein距离计算模块；4) 梯度匹配模块；5) 多损失目标函数。训练过程中，首先计算教师模型和学生模型的输出特征，然后使用Wasserstein距离衡量特征差异，并进行梯度匹配。Gompertz曲线根据训练epoch动态调整蒸馏损失的权重，最后通过多损失目标函数优化学生模型。

**关键创新**：最重要的技术创新点在于将Gompertz增长模型引入知识蒸馏框架，并利用Gompertz曲线动态调整蒸馏损失的权重。与传统方法相比，Gompertz-CNN能够更好地适应学生模型的学习过程，从而提高知识传递的效率和最终性能。此外，结合Wasserstein距离和梯度匹配进一步提升了知识传递的质量。

**关键设计**：Gompertz曲线的参数需要根据具体任务进行调整，例如曲线的增长速率和饱和值。Wasserstein距离用于衡量教师模型和学生模型在特征层面的差异，可以采用不同的距离度量方式。梯度匹配通过最小化教师模型和学生模型梯度之间的差异来实现，可以采用不同的梯度对齐策略。多损失目标函数将分类损失、蒸馏损失、Wasserstein距离损失和梯度匹配损失进行加权组合，需要仔细调整各个损失的权重。

## 📊 实验亮点

实验结果表明，Gompertz-CNN在CIFAR-10和CIFAR-100数据集上均取得了显著的性能提升。在CIFAR-10上，Gompertz-CNN相比传统知识蒸馏方法，准确率提升高达8%。在CIFAR-100上，准确率提升高达4%。这些结果表明，Gompertz-CNN能够有效提高学生模型的性能，并优于传统的知识蒸馏方法。

## 🎯 应用场景

Gompertz-CNN可应用于各种需要模型压缩和加速的场景，例如移动设备上的图像识别、自动驾驶中的目标检测、以及资源受限环境下的模型部署。该方法能够有效提升学生模型的性能，使其在保持较低计算复杂度的同时，达到接近教师模型的精度。未来可进一步探索其在自然语言处理等领域的应用。

## 📄 摘要（原文）

> This paper introduces a novel dynamic knowledge distillation framework, Gompertz-CNN, which integrates the Gompertz growth model into the training process to address the limitations of traditional knowledge distillation. Conventional methods often fail to capture the evolving cognitive capacity of student models, leading to suboptimal knowledge transfer. To overcome this, we propose a stage-aware distillation strategy that dynamically adjusts the weight of distillation loss based on the Gompertz curve, reflecting the student's learning progression: slow initial growth, rapid mid-phase improvement, and late-stage saturation. Our framework incorporates Wasserstein distance to measure feature-level discrepancies and gradient matching to align backward propagation behaviors between teacher and student models. These components are unified under a multi-loss objective, where the Gompertz curve modulates the influence of distillation losses over time. Extensive experiments on CIFAR-10 and CIFAR-100 using various teacher-student architectures (e.g., ResNet50 and MobileNet_v2) demonstrate that Gompertz-CNN consistently outperforms traditional distillation methods, achieving up to 8% and 4% accuracy gains on CIFAR-10 and CIFAR-100, respectively.

