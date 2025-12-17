---
layout: default
title: Pick-to-Learn for Systems and Control: Data-driven Synthesis with State-of-the-art Safety Guarantees
---

# Pick-to-Learn for Systems and Control: Data-driven Synthesis with State-of-the-art Safety Guarantees

**arXiv**: [2512.04781v1](https://arxiv.org/abs/2512.04781) | [PDF](https://arxiv.org/pdf/2512.04781.pdf)

**作者**: Dario Paccagnan, Daniel Marks, Marco C. Campi, Simone Garatti

---

## 💡 一句话要点

**提出Pick-to-Learn框架，为数据驱动控制方法提供安全与性能保证，无需预留校准数据。**

**关键词**: `数据驱动控制` `安全保证` `Pick-to-Learn` `系统合成` `性能优化`

## 📋 核心要点

1. 核心问题：数据驱动控制在安全关键环境中需保证安全，但现有方法常牺牲数据或限制算法，导致性能不佳。
2. 方法要点：P2L框架允许任何数据驱动控制方法联合合成与认证设计，利用全部数据，无需预留校准或验证数据。
3. 实验或效果：在最优控制、可达性分析等核心问题中，P2L提供优于常用方法的设计与证书，展示广泛适用潜力。

## 📄 摘要（原文）

> Data-driven methods have become paramount in modern systems and control problems characterized by growing levels of complexity. In safety-critical environments, deploying these methods requires rigorous guarantees, a need that has motivated much recent work at the interface of statistical learning and control. However, many existing approaches achieve this goal at the cost of sacrificing valuable data for testing and calibration, or by constraining the choice of learning algorithm, thus leading to suboptimal performances. In this paper, we describe Pick-to-Learn (P2L) for Systems and Control, a framework that allows any data-driven control method to be equipped with state-of-the-art safety and performance guarantees. P2L enables the use of all available data to jointly synthesize and certify the design, eliminating the need to set aside data for calibration or validation purposes. In presenting a comprehensive version of P2L for systems and control, this paper demonstrates its effectiveness across a range of core problems, including optimal control, reachability analysis, safe synthesis, and robust control. In many of these applications, P2L delivers designs and certificates that outperform commonly employed methods, and shows strong potential for broad applicability in diverse practical settings.

