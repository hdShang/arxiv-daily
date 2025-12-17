---
layout: default
title: Reducing Robotic Upper-Limb Assessment Time While Maintaining Precision: A Time Series Foundation Model Approach
---

# Reducing Robotic Upper-Limb Assessment Time While Maintaining Precision: A Time Series Foundation Model Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00193" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00193v1</a>
  <a href="https://arxiv.org/pdf/2511.00193.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00193v1" onclick="toggleFavorite(this, '2511.00193v1', 'Reducing Robotic Upper-Limb Assessment Time While Maintaining Precision: A Time Series Foundation Model Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Faranak Akbarifar, Nooshin Maghsoodi, Sean P Dukelow, Stephen Scott, Parvin Mousavi

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-31

---

## 💡 一句话要点

**利用时序基础模型，在保证精度的前提下，缩短机器人上肢评估时间**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人评估` `上肢运动功能` `时序预测` `基础模型` `运动学参数`

## 📋 核心要点

1. Kinarm机器人VGR评估虽然能提供敏感的运动学指标，但需要大量的抓取试验，导致耗时和疲劳。
2. 本研究利用时序基础模型预测未记录的试验，从而减少实际需要的抓取次数，同时保持运动学参数的可靠性。
3. 实验结果表明，使用Chronos模型预测，仅需8次实际抓取即可达到与24-28次抓取相当的可靠性，显著缩短评估时间。

## 📝 摘要（中文）

本研究旨在缩短Kinarm机器人上视觉引导抓取(VGR)评估时间，该评估虽能产生敏感的运动学生物标志物，但需40-64次抓取，造成时间和疲劳负担。我们评估了时序基础模型是否能在仅记录少量早期抓取试验的情况下，通过预测未记录的试验来保持标准Kinarm参数的可靠性。我们分析了来自461名中风患者和599名对照参与者的VGR速度信号，这些数据来自4目标和8目标抓取协议。我们仅保留前8或16次抓取试验，并使用ARIMA、MOMENT和Chronos模型（在70%的受试者上进行微调）来预测合成试验。我们重新计算了抓取的四个运动学特征（反应时间、运动时间、姿势速度、最大速度），这些特征基于记录的试验和预测的试验的组合，并使用ICC(2,1)将其与完整长度的参考进行比较。结果表明，仅使用8次记录的试验加上Chronos预测，所有参数的ICC均恢复到>=0.90，与24-28次记录的抓取的可靠性相当（Delta ICC <= 0.07）。MOMENT产生了中等程度的增益，而ARIMA的改进最小。在不同的队列和协议中，合成试验在不显著影响特征可靠性的情况下替代了抓取试验。结论是，基础模型预测可以大大缩短Kinarm VGR评估时间。对于受损最严重的中风幸存者，评估时间从4-5分钟降至约1分钟，同时保持了运动学精度。这种预测增强的范例有望实现高效的机器人评估，以评估中风后的运动障碍。

## 🔬 方法详解

**问题定义**：本研究旨在解决机器人上肢运动功能评估中，传统方法耗时过长的问题。现有的Kinarm机器人VGR评估需要进行大量的抓取试验，这对于患者，特别是中风患者，会造成较大的时间和疲劳负担，影响评估的效率和准确性。

**核心思路**：核心思路是利用时序预测模型，根据少量（例如8次或16次）的早期抓取试验数据，预测后续的抓取轨迹，从而减少实际需要的抓取次数。这样可以在保证运动学参数可靠性的前提下，显著缩短评估时间。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据采集：使用Kinarm机器人进行VGR评估，记录参与者的速度信号。2) 数据预处理：选取前8次或16次抓取试验的数据作为输入，其余数据作为验证。3) 模型训练：使用ARIMA、MOMENT和Chronos三种时序模型，在70%的受试者数据上进行微调。4) 试验预测：使用训练好的模型预测剩余的抓取试验轨迹。5) 参数计算与评估：基于实际记录和预测的轨迹，计算运动学参数（反应时间、运动时间、姿势速度、最大速度），并使用ICC(2,1)评估其可靠性。

**关键创新**：最重要的技术创新点在于将时序基础模型应用于机器人运动功能评估领域，并验证了其在减少评估时间的同时保持精度的有效性。与传统的统计模型（如ARIMA）相比，基础模型（如Chronos和MOMENT）具有更强的时序建模能力，能够更准确地预测抓取轨迹。

**关键设计**：关键设计包括：1) 模型选择：选择了ARIMA、MOMENT和Chronos三种时序模型进行比较，其中Chronos表现最佳。2) 数据划分：将数据划分为训练集（70%的受试者）和测试集（30%的受试者），用于模型训练和评估。3) 评估指标：使用ICC(2,1)作为评估运动学参数可靠性的指标。4) 试验次数：对比了使用8次和16次实际抓取试验进行预测的效果。

## 📊 实验亮点

实验结果表明，使用Chronos模型，仅需8次记录的抓取试验加上预测的试验，即可使所有运动学参数的ICC恢复到>=0.90，与24-28次记录的抓取的可靠性相当（Delta ICC <= 0.07）。对于受损最严重的中风幸存者，评估时间从4-5分钟降至约1分钟，显著提高了评估效率。

## 🎯 应用场景

该研究成果可广泛应用于中风、脑瘫等神经系统疾病患者的上肢运动功能评估。通过缩短评估时间，可以减轻患者的负担，提高评估效率，并为康复治疗方案的制定提供更及时、准确的依据。此外，该方法还可以推广到其他需要重复性动作的机器人评估场景，例如下肢运动功能评估、平衡能力评估等。

## 📄 摘要（原文）

> Purpose: Visually Guided Reaching (VGR) on the Kinarm robot yields sensitive kinematic biomarkers but requires 40-64 reaches, imposing time and fatigue burdens. We evaluate whether time-series foundation models can replace unrecorded trials from an early subset of reaches while preserving the reliability of standard Kinarm parameters.
>   Methods: We analyzed VGR speed signals from 461 stroke and 599 control participants across 4- and 8-target reaching protocols. We withheld all but the first 8 or 16 reaching trials and used ARIMA, MOMENT, and Chronos models, fine-tuned on 70 percent of subjects, to forecast synthetic trials. We recomputed four kinematic features of reaching (reaction time, movement time, posture speed, maximum speed) on combined recorded plus forecasted trials and compared them to full-length references using ICC(2,1).
>   Results: Chronos forecasts restored ICC >= 0.90 for all parameters with only 8 recorded trials plus forecasts, matching the reliability of 24-28 recorded reaches (Delta ICC <= 0.07). MOMENT yielded intermediate gains, while ARIMA improvements were minimal. Across cohorts and protocols, synthetic trials replaced reaches without materially compromising feature reliability.
>   Conclusion: Foundation-model forecasting can greatly shorten Kinarm VGR assessment time. For the most impaired stroke survivors, sessions drop from 4-5 minutes to about 1 minute while preserving kinematic precision. This forecast-augmented paradigm promises efficient robotic evaluations for assessing motor impairments following stroke.

