---
layout: default
title: Robustness Evaluation of Machine Learning Models for Fault Classification and Localization In Power System Protection
---

# Robustness Evaluation of Machine Learning Models for Fault Classification and Localization In Power System Protection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15385" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15385v1</a>
  <a href="https://arxiv.org/pdf/2512.15385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15385v1" onclick="toggleFavorite(this, '2512.15385v1', 'Robustness Evaluation of Machine Learning Models for Fault Classification and Localization In Power System Protection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Julian Oelhaf, Mehran Pashaei, Georg Kordowich, Christian Bergler, Andreas Maier, Johann Jäger, Siming Bayer

**分类**: cs.LG, eess.SP

**发布日期**: 2025-12-17

**备注**: This paper is a postprint of a paper submitted to and accepted for publication in the 20th IET International Conference on Developments in Power System Protection (DPSP Global 2026) and is subject to Institution of Engineering and Technology Copyright. The copy of record is available at the IET Digital Library

---

## 💡 一句话要点

**提出电力系统保护中机器学习模型鲁棒性评估框架，解决恶劣工况下的可靠性问题。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `电力系统保护` `机器学习` `鲁棒性评估` `故障分类` `故障定位` `传感器退化` `EMT仿真`

## 📋 核心要点

1. 传统电力系统保护方案难以适应可再生能源带来的变化，需要更智能的故障分类与定位方法。
2. 论文提出统一的鲁棒性评估框架，通过模拟传感器退化场景，评估机器学习模型在电力系统保护中的可靠性。
3. 实验结果表明，故障分类对多数退化情况稳定，但单相损耗影响较大；故障定位对电压损耗更敏感。

## 📝 摘要（中文）

随着可再生能源和分布式发电日益普及，电力系统正经历转型，对依赖固定设置和本地测量的传统保护方案提出了挑战。机器学习(ML)为集中式故障分类(FC)和故障定位(FL)提供了一种数据驱动的替代方案，从而能够更快、更自适应地进行决策。然而，实际部署的关键在于鲁棒性。即使面对缺失、嘈杂或退化的传感器数据，保护算法也必须保持可靠。本研究提出了一个统一的框架，用于系统地评估电力系统保护中ML模型的鲁棒性。使用高保真EMT仿真来模拟真实的退化场景，包括传感器中断、降低的采样率和瞬态通信丢失。该框架为基准测试模型、量化有限可观测性的影响以及识别弹性运行所需的关键测量通道提供了一致的方法。结果表明，FC在大多数退化类型下保持高度稳定，但在单相损耗下下降约13%，而FL总体上更敏感，电压损耗使定位误差增加150%以上。这些发现为未来ML辅助保护系统的鲁棒性设计提供了可操作的指导。

## 🔬 方法详解

**问题定义**：电力系统保护依赖的传统方法难以适应新能源渗透带来的复杂性，机器学习模型虽然提供了新的可能性，但其在实际部署中面临传感器数据质量下降（如缺失、噪声、低采样率）带来的鲁棒性挑战。现有方法缺乏系统性的鲁棒性评估框架，难以保证模型在恶劣工况下的可靠性。

**核心思路**：论文的核心思路是构建一个统一的框架，通过高保真仿真模拟各种传感器退化场景，系统地评估机器学习模型在故障分类和故障定位任务中的鲁棒性。通过量化不同退化场景对模型性能的影响，识别关键的测量通道，为鲁棒性感知的设计提供指导。

**技术框架**：该框架主要包含以下几个阶段：1) 使用高保真EMT仿真生成电力系统数据，模拟正常和故障工况；2) 引入各种传感器退化场景，如传感器中断、降低采样率、瞬态通信丢失等；3) 使用机器学习模型进行故障分类和故障定位；4) 评估模型在不同退化场景下的性能，量化鲁棒性；5) 分析结果，识别关键测量通道。

**关键创新**：该论文的关键创新在于提出了一个统一的、系统性的鲁棒性评估框架，能够量化不同类型传感器退化对电力系统保护中机器学习模型性能的影响。该框架不仅可以用于评估现有模型的鲁棒性，还可以指导未来鲁棒性感知模型的开发。与以往研究相比，该框架更加全面和系统，考虑了多种实际的传感器退化场景。

**关键设计**：论文使用了高保真EMT仿真来模拟电力系统，保证了数据的真实性和可靠性。在传感器退化方面，考虑了传感器中断、降低采样率、瞬态通信丢失等多种实际情况。机器学习模型方面，可以选择不同的模型进行评估，例如支持向量机、神经网络等。评估指标方面，使用了故障分类的准确率和故障定位的误差等指标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15385v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15385v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15385v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，故障分类模型在大多数传感器退化情况下表现出较强的鲁棒性，但在单相损耗情况下，准确率下降约13%。故障定位模型对电压损耗更为敏感，定位误差增加超过150%。这些数据清晰地展示了不同类型传感器退化对模型性能的影响，为实际应用提供了重要参考。

## 🎯 应用场景

该研究成果可应用于智能电网的故障诊断与自愈，提升电力系统在复杂和恶劣环境下的运行可靠性。通过鲁棒性评估，可以指导电力系统保护装置的设计和优化，降低因传感器故障或数据质量问题导致的误判风险，保障电力系统的安全稳定运行。未来，该框架可扩展到其他电力系统应用，如状态估计和预测。

## 📄 摘要（原文）

> The growing penetration of renewable and distributed generation is transforming power systems and challenging conventional protection schemes that rely on fixed settings and local measurements. Machine learning (ML) offers a data-driven alternative for centralized fault classification (FC) and fault localization (FL), enabling faster and more adaptive decision-making. However, practical deployment critically depends on robustness. Protection algorithms must remain reliable even when confronted with missing, noisy, or degraded sensor data. This work introduces a unified framework for systematically evaluating the robustness of ML models in power system protection.
>   High-fidelity EMT simulations are used to model realistic degradation scenarios, including sensor outages, reduced sampling rates, and transient communication losses. The framework provides a consistent methodology for benchmarking models, quantifying the impact of limited observability, and identifying critical measurement channels required for resilient operation. Results show that FC remains highly stable under most degradation types but drops by about 13% under single-phase loss, while FL is more sensitive overall, with voltage loss increasing localization error by over 150%. These findings offer actionable guidance for robustness-aware design of future ML-assisted protection systems.

