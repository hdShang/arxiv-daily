---
layout: default
title: Context-aware deep learning using individualized prior information reduces false positives in disease risk prediction and longitudinal health assessment
---

# Context-aware deep learning using individualized prior information reduces false positives in disease risk prediction and longitudinal health assessment

**arXiv**: [2510.15591v1](https://arxiv.org/abs/2510.15591) | [PDF](https://arxiv.org/pdf/2510.15591.pdf)

**作者**: Lavanya Umapathy, Patricia M Johnson, Tarun Dutt, Angela Tong, Madhur Nayan, Hersh Chandarana, Daniel K Sodickson

---

## 💡 一句话要点

**提出上下文感知深度学习框架，整合历史医疗数据以降低疾病风险预测的假阳性率**

**关键词**: `上下文感知深度学习` `疾病风险预测` `假阳性率降低` `纵向健康评估` `前列腺癌预测` `医疗数据整合`

## 📋 核心要点

1. 核心问题：医疗时间上下文利用不足，导致疾病风险预测假阳性率高。
2. 方法要点：结合最近和先前访问数据，先估计初始风险，再通过历史信息精炼。
3. 实验或效果：在前列腺癌预测中，假阳性率从51%降至24%，特异性提升。

## 📄 摘要（原文）

> Temporal context in medicine is valuable in assessing key changes in patient
> health over time. We developed a machine learning framework to integrate
> diverse context from prior visits to improve health monitoring, especially when
> prior visits are limited and their frequency is variable. Our model first
> estimates initial risk of disease using medical data from the most recent
> patient visit, then refines this assessment using information digested from
> previously collected imaging and/or clinical biomarkers. We applied our
> framework to prostate cancer (PCa) risk prediction using data from a large
> population (28,342 patients, 39,013 magnetic resonance imaging scans, 68,931
> blood tests) collected over nearly a decade. For predictions of the risk of
> clinically significant PCa at the time of the visit, integrating prior context
> directly converted false positives to true negatives, increasing overall
> specificity while preserving high sensitivity. False positive rates were
> reduced progressively from 51% to 33% when integrating information from up to
> three prior imaging examinations, as compared to using data from a single
> visit, and were further reduced to 24% when also including additional context
> from prior clinical data. For predicting the risk of PCa within five years of
> the visit, incorporating prior context reduced false positive rates still
> further (64% to 9%). Our findings show that information collected over time
> provides relevant context to enhance the specificity of medical risk
> prediction. For a wide range of progressive conditions, sufficient reduction of
> false positive rates using context could offer a pathway to expand longitudinal
> health monitoring programs to large populations with comparatively low baseline
> risk of disease, leading to earlier detection and improved health outcomes.

