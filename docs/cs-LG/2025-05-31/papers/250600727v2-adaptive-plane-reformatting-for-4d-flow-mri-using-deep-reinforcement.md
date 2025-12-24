---
layout: default
title: Adaptive Plane Reformatting for 4D Flow MRI using Deep Reinforcement Learning
---

# Adaptive Plane Reformatting for 4D Flow MRI using Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00727" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00727v2</a>
  <a href="https://arxiv.org/pdf/2506.00727.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00727v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00727v2', 'Adaptive Plane Reformatting for 4D Flow MRI using Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javier Bisbal, Julio Sotelo, Maria I Valdés, Pablo Irarrazaval, Marcelo E Andia, Julio García, José Rodriguez-Palomarez, Francesca Raimondi, Cristián Tejos, Sergio Uribe

**分类**: cs.LG, cs.CV

**发布日期**: 2025-05-31 (更新: 2025-12-01)

---

## 💡 一句话要点

**提出AdaPR以解决4D流MRI重建中的适应性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `4D流MRI` `平面重建` `医学成像` `适应性算法` `心血管流动` `局部坐标系统`

## 📋 核心要点

1. 现有的4D流MRI平面重建方法耗时且受观察者差异影响，限制了心血管流动的快速评估。
2. 论文提出的AdaPR框架利用深度强化学习，通过局部坐标系统实现对任意位置和方向的体积导航。
3. 实验结果显示，AdaPR在不同体积方向和位置下保持一致的准确性，流量测量与手动观察者结果高度相关。

## 📝 摘要（中文）

背景与目标：四维相位对比MRI（4D流MRI）的平面重建耗时且易受观察者差异影响，限制了心血管流动的快速评估。深度强化学习（DRL）能够训练代理迭代调整平面位置和方向，实现准确的平面重建。现有DRL方法假设测试体积与训练数据具有相同的空间对齐，限制了跨扫描仪和机构的泛化能力。为了解决这一限制，我们提出了AdaPR（自适应平面重建），一个使用局部坐标系统导航任意位置和方向体积的DRL框架。方法：我们使用异步优势演员-评论家（A3C）算法实现了AdaPR，并在88个来自多个供应商的4D流MRI数据集上进行了验证。结果：AdaPR的平均角度误差为6.32±4.15度，距离误差为3.40±2.75毫米，优于全局坐标DRL方法和其他非DRL方法。结论：AdaPR提供了稳健的、与方向无关的4D流MRI平面重建，流量量化结果与专家观察者相当，具有广泛的医学成像应用潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决4D流MRI平面重建中的适应性问题，现有方法在不同扫描仪和数据集上泛化能力不足，导致重建效果不稳定。

**核心思路**：提出的AdaPR框架通过深度强化学习，利用局部坐标系统来调整平面位置和方向，从而实现对任意体积的适应性重建。

**技术框架**：AdaPR基于异步优势演员-评论家（A3C）算法，包含数据预处理、模型训练和重建三个主要模块。训练过程中，代理通过与环境交互不断优化平面调整策略。

**关键创新**：AdaPR的核心创新在于其局部坐标系统的使用，使得模型能够在不同的体积位置和方向下进行有效的平面重建，克服了传统方法的局限性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化平面重建的准确性，并通过多样化的训练数据集增强模型的泛化能力。

## 📊 实验亮点

实验结果显示，AdaPR在88个4D流MRI数据集上的平均角度误差为6.32度，距离误差为3.40毫米，显著优于传统的全局坐标DRL方法和其他非DRL方法。流量测量结果与手动观察者的结果高度相关，表明其在临床应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医学成像、心血管疾病的诊断与监测等。AdaPR的适应性和准确性使其在不同设备和数据集上均能有效工作，未来有望推广至其他医学成像技术中。

## 📄 摘要（原文）

> Background and Objective: Plane reformatting for four-dimensional phase contrast MRI (4D flow MRI) is time-consuming and prone to inter-observer variability, which limits fast cardiovascular flow assessment. Deep reinforcement learning (DRL) trains agents to iteratively adjust plane position and orientation, enabling accurate plane reformatting without the need for detailed landmarks, making it suitable for images with limited contrast and resolution such as 4D flow MRI. However, current DRL methods assume that test volumes share the same spatial alignment as the training data, limiting generalization across scanners and institutions. To address this limitation, we introduce AdaPR (Adaptive Plane Reformatting), a DRL framework that uses a local coordinate system to navigate volumes with arbitrary positions and orientations.
>   Methods: We implemented AdaPR using the Asynchronous Advantage Actor-Critic (A3C) algorithm and validated it on 88 4D flow MRI datasets acquired from multiple vendors, including patients with congenital heart disease.
>   Results: AdaPR achieved a mean angular error of 6.32 +/- 4.15 degrees and a distance error of 3.40 +/- 2.75 mm, outperforming global-coordinate DRL methods and alternative non-DRL methods. AdaPR maintained consistent accuracy under different volume orientations and positions. Flow measurements from AdaPR planes showed no significant differences compared to two manual observers, with excellent correlation (R^2 = 0.972 and R^2 = 0.968), comparable to inter-observer agreement (R^2 = 0.969).
>   Conclusion: AdaPR provides robust, orientation-independent plane reformatting for 4D flow MRI, achieving flow quantification comparable to expert observers. Its adaptability across datasets and scanners makes it a promising candidate for medical imaging applications beyond 4D flow MRI.

