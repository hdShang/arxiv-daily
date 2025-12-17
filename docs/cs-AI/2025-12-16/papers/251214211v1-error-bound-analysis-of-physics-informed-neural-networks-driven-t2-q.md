---
layout: default
title: Error Bound Analysis of Physics-Informed Neural Networks-Driven T2 Quantification in Cardiac Magnetic Resonance Imaging
---

# Error Bound Analysis of Physics-Informed Neural Networks-Driven T2 Quantification in Cardiac Magnetic Resonance Imaging

**arXiv**: [2512.14211v1](https://arxiv.org/abs/2512.14211) | [PDF](https://arxiv.org/pdf/2512.14211.pdf)

**作者**: Mengxue Zhang, Qingrui Cai, Yinyin Chen, Hang Jin, Jianjun Zhou, Qiu Guo, Peijun Zhao, Zhiping Mao, Xingxing Zhang, Yuyu Xia, Xianwang Jiang, Qin Xu, Chunyan Xiong, Yirong Zhou, Chengyan Wang, Xiaobo Qu

**分类**: physics.bio-ph, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于物理信息神经网络的T2量化方法，通过误差界分析解决心脏磁共振成像中定量参数估计的理论与数据挑战。**

**关键词**: `物理信息神经网络` `T2量化` `心脏磁共振成像` `误差界分析` `布洛赫方程` `定量参数估计` `急性心肌梗死` `理论保障`

## 📋 核心要点

1. 现有深度学习方法依赖大量训练数据且缺乏理论支持，难以在无金标准下评估T2定量准确性。
2. 提出将布洛赫方程嵌入PINN损失，仅基于扫描数据实现T2估计，无需预训练数据库。
3. 在数值模型和临床患者中验证方法，实现低误差T2量化，理论误差界为评估提供依据。

## 📝 摘要（中文）

物理信息神经网络（PINN）正成为磁共振成像（MRI）定量参数估计的一种有前景方法。现有深度学习方法虽能提供T2参数的准确定量估计，但仍需大量训练数据，且缺乏理论支持和公认的金标准。鉴于目前尚无基于PINN的T2估计方法，我们提出将MRI基本物理原理——布洛赫方程嵌入PINN的损失函数中，该方法仅基于目标扫描数据，无需预定义训练数据库。此外，通过推导T2估计误差和布洛赫方程解泛化误差的严格上界，我们为评估PINN定量准确性建立了理论基础。即使无法获取真实值或金标准，该理论也能估计相对于真实定量参数T2的误差。在数值心脏模型和水模上验证了T2映射的准确性及理论分析的有效性，我们的方法在心肌T2范围内表现出优异的定量精度。在94例急性心肌梗死（AMI）患者中证实了临床适用性，在理论误差界内实现了低误差的定量T2估计，突显了PINN的稳健性和潜力。

## 🔬 方法详解

论文提出基于物理信息神经网络（PINN）的T2量化框架，核心是将MRI的布洛赫方程作为物理约束嵌入神经网络的损失函数中。关键创新点在于推导了T2估计误差和布洛赫方程解泛化误差的严格上界，为PINN的定量准确性提供了理论保障。与现有深度学习方法相比，该方法无需大量训练数据，仅依赖目标扫描数据，通过物理原理引导网络学习，实现了数据高效且理论可解释的T2参数估计。

## 📊 实验亮点

在数值心脏模型和水模实验中，方法在心肌T2范围内表现出优异定量精度；在94例急性心肌梗死患者临床验证中，实现低误差T2估计，且结果符合理论误差界，证实了方法的有效性和临床潜力。

## 🎯 应用场景

该方法主要应用于心脏磁共振成像中的T2定量参数估计，特别适用于急性心肌梗死等心脏疾病的诊断和监测。通过提供理论误差界，可在无金标准情况下评估定量准确性，增强临床应用的可靠性和稳健性，推动精准医疗发展。

## 📄 摘要（原文）

> Physics-Informed Neural Networks (PINN) are emerging as a promising approach for quantitative parameter estimation of Magnetic Resonance Imaging (MRI). While existing deep learning methods can provide an accurate quantitative estimation of the T2 parameter, they still require large amounts of training data and lack theoretical support and a recognized gold standard. Thus, given the absence of PINN-based approaches for T2 estimation, we propose embedding the fundamental physics of MRI, the Bloch equation, in the loss of PINN, which is solely based on target scan data and does not require a pre-defined training database. Furthermore, by deriving rigorous upper bounds for both the T2 estimation error and the generalization error of the Bloch equation solution, we establish a theoretical foundation for evaluating the PINN's quantitative accuracy. Even without access to the ground truth or a gold standard, this theory enables us to estimate the error with respect to the real quantitative parameter T2. The accuracy of T2 mapping and the validity of the theoretical analysis are demonstrated on a numerical cardiac model and a water phantom, where our method exhibits excellent quantitative precision in the myocardial T2 range. Clinical applicability is confirmed in 94 acute myocardial infarction (AMI) patients, achieving low-error quantitative T2 estimation under the theoretical error bound, highlighting the robustness and potential of PINN.

