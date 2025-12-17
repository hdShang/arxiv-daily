---
layout: default
title: Evaluating Adversarial Attacks on Federated Learning for Temperature Forecasting
---

# Evaluating Adversarial Attacks on Federated Learning for Temperature Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13207" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13207</a>
  <a href="https://arxiv.org/pdf/2512.13207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13207" onclick="toggleFavorite(this, '2512.13207', 'Evaluating Adversarial Attacks on Federated Learning for Temperature Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karina Chichifoi, Fabio Merizzi, Michele Colajanni

**分类**: cs.LG, cs.CR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**研究联邦学习在温度预测中对抗攻击的脆弱性，揭示空间依赖性带来的安全风险。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `联邦学习` `对抗攻击` `数据投毒` `温度预测` `空间依赖性` `气象预测` `安全性` `修剪均值`

## 📋 核心要点

1. 联邦学习在气象预测中面临数据投毒攻击的威胁，攻击者通过恶意数据影响全局模型，现有研究缺乏对空间依赖性影响的深入分析。
2. 该研究模拟地理分布式客户端，评估全局偏差和局部补丁攻击对联邦学习温度预测的影响，分析攻击对预测结果的扭曲程度。
3. 实验表明，少量中毒客户端即可显著影响大范围区域的温度预测，修剪均值防御对全局偏差攻击有效，但对局部补丁攻击失效。

## 📝 摘要（中文）

深度学习和联邦学习（FL）正成为下一代天气预报的强大伙伴。深度学习能够实现超越传统数值模型的高分辨率时空预测，而FL允许不同地点的机构协作训练模型，无需共享原始数据，从而解决效率和安全问题。虽然FL在异构区域显示出前景，但其分布式特性引入了新的漏洞。特别是，数据投毒攻击，即受损客户端注入被操纵的训练数据，会降低性能或引入系统性偏差。气象数据中的空间依赖性加剧了这些威胁，使得局部扰动可以通过全局模型聚合影响更广泛的区域。本研究调查了对抗性客户端如何扭曲基于哥白尼欧洲区域再分析（CERRA）数据集训练的联邦地表温度预测。我们模拟了地理上分布的客户端，并评估了基于补丁和全局偏差的攻击对区域温度预测的影响。结果表明，即使一小部分中毒客户端也会误导大范围空间连接区域的预测。来自单个受损客户端的全局温度偏差攻击使预测偏移高达-1.7 K，而协调的补丁攻击使均方误差增加三倍以上，并产生超过+3.5 K的持续区域异常。最后，我们评估了修剪均值聚合作为一种防御机制，表明它可以成功防御全局偏差攻击（2-13%的降级），但对补丁攻击无效（281-603%的放大），暴露了基于异常值的防御在空间相关数据方面的局限性。

## 🔬 方法详解

**问题定义**：论文旨在研究联邦学习在温度预测任务中，面对恶意客户端的数据投毒攻击时的脆弱性。现有方法忽略了气象数据的空间依赖性，导致攻击效果被低估，防御策略设计不足。攻击者可以通过操纵局部数据，影响全局模型的预测精度和可靠性。

**核心思路**：论文的核心思路是模拟现实世界中地理位置分散的客户端，并设计不同类型的对抗性攻击（全局偏差和局部补丁攻击），评估这些攻击对联邦学习模型预测结果的影响。通过分析攻击造成的误差和异常，揭示联邦学习在气象预测中的安全风险。

**技术框架**：整体框架包括以下几个主要步骤：1) 数据集准备：使用哥白尼欧洲区域再分析（CERRA）数据集，模拟地理分布式客户端的数据；2) 模型训练：使用联邦学习算法训练温度预测模型；3) 攻击模拟：模拟恶意客户端，注入全局偏差或局部补丁攻击；4) 评估：评估攻击对模型预测结果的影响，包括均方误差、温度偏差等指标；5) 防御：评估修剪均值聚合作为防御机制的有效性。

**关键创新**：论文的关键创新在于：1) 关注气象数据的空间依赖性，设计了更贴近实际场景的局部补丁攻击；2) 深入分析了不同类型攻击对联邦学习模型的影响，揭示了现有防御机制的局限性；3) 提出了针对空间相关数据的联邦学习安全风险评估方法。

**关键设计**：论文的关键设计包括：1) 全局偏差攻击：恶意客户端将所有温度数据加上一个固定的偏差值；2) 局部补丁攻击：恶意客户端在局部区域的温度数据中注入异常值，模拟局部极端天气事件；3) 修剪均值聚合：一种常用的联邦学习防御机制，通过剔除异常客户端的更新来提高模型的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13207/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13207/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13207/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，单个恶意客户端的全局温度偏差攻击可导致预测偏移高达-1.7 K，协调的局部补丁攻击使均方误差增加三倍以上，并产生超过+3.5 K的持续区域异常。修剪均值聚合可以有效防御全局偏差攻击（2-13%的降级），但对局部补丁攻击无效（281-603%的放大）。

## 🎯 应用场景

该研究成果可应用于提升联邦学习在气象预测领域的安全性，例如设计更有效的防御机制，提高模型对恶意攻击的鲁棒性。此外，该研究方法也可推广到其他具有空间依赖性的联邦学习应用场景，如环境监测、智慧城市等，为保障数据安全和模型可靠性提供参考。

## 📄 摘要（原文）

> Deep learning and federated learning (FL) are becoming powerful partners for next-generation weather forecasting. Deep learning enables high-resolution spatiotemporal forecasts that can surpass traditional numerical models, while FL allows institutions in different locations to collaboratively train models without sharing raw data, addressing efficiency and security concerns. While FL has shown promise across heterogeneous regions, its distributed nature introduces new vulnerabilities. In particular, data poisoning attacks, in which compromised clients inject manipulated training data, can degrade performance or introduce systematic biases. These threats are amplified by spatial dependencies in meteorological data, allowing localized perturbations to influence broader regions through global model aggregation. In this study, we investigate how adversarial clients distort federated surface temperature forecasts trained on the Copernicus European Regional ReAnalysis (CERRA) dataset. We simulate geographically distributed clients and evaluate patch-based and global biasing attacks on regional temperature forecasts. Our results show that even a small fraction of poisoned clients can mislead predictions across large, spatially connected areas. A global temperature bias attack from a single compromised client shifts predictions by up to -1.7 K, while coordinated patch attacks more than triple the mean squared error and produce persistent regional anomalies exceeding +3.5 K. Finally, we assess trimmed mean aggregation as a defense mechanism, showing that it successfully defends against global bias attacks (2-13% degradation) but fails against patch attacks (281-603% amplification), exposing limitations of outlier-based defenses for spatially correlated data.

