---
layout: default
title: Early Warning Index for Patient Deteriorations in Hospitals
---

# Early Warning Index for Patient Deteriorations in Hospitals

**arXiv**: [2512.14683v1](https://arxiv.org/abs/2512.14683) | [PDF](https://arxiv.org/pdf/2512.14683.pdf)

**作者**: Dimitris Bertsimas, Yu Ma, Kimberly Villalobos Carballo, Gagan Singh, Michal Laskowski, Jeff Mather, Dan Kombert, Howard Haronian

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出早期预警指数（EWI）多模态机器学习框架，以解决医院患者病情恶化预测难题。**

**关键词**: `早期预警指数` `多模态机器学习` `患者恶化预测` `可解释人工智能` `电子健康记录` `临床决策支持` `医院运营优化` `风险分层`

## 📋 核心要点

1. 核心问题：医院缺乏自动化系统整合异构临床数据，难以准确预测患者病情恶化，数据格式不一致导致风险评估挑战。
2. 方法要点：开发多模态机器学习框架EWI，结合人机协同过程，利用SHAP增强可解释性，自动提取EHR特征预测综合风险。
3. 实验或效果：在18,633名患者数据集上实现C统计量0.796，部署为医院仪表板，有效分类患者风险，提升护理效率。

## 📝 摘要（中文）

医院缺乏自动化系统来利用日益增长的异构临床和运营数据有效预测关键事件。早期识别有恶化风险的患者不仅对患者护理质量监控至关重要，也对医生护理管理至关重要。然而，由于数据格式不一致，将各种数据流转化为准确且可解释的风险评估面临重大挑战。我们开发了一个多模态机器学习框架——早期预警指数（EWI），用于预测ICU入院、紧急响应团队派遣和死亡率的综合风险。EWI设计的关键在于人机协同过程：临床医生帮助确定警报阈值并解释模型输出，这些输出通过使用SHAP（Shapley Additive exPlanations）的可解释性增强，以突出驱动每位患者风险的临床和运营因素（如计划手术、病房普查）。我们将EWI部署在医院仪表板中，将患者分为三个风险等级。使用美国一家大型医院的18,633名独特患者数据集，我们的方法从结构化和非结构化电子健康记录（EHR）数据中自动提取特征，并实现了0.796的C统计量。目前，它被用作主动管理风险患者的分类工具。所提出的方法通过自动对不同风险水平的患者进行排序，为医生节省了宝贵时间，使他们能够专注于患者护理，而不是筛选复杂的EHR数据。通过进一步精确定位特定风险驱动因素，该模型为护理人员调度和关键资源分配提供了数据驱动的调整。因此，临床医生和管理人员可以避免下游并发症，包括昂贵的手术或高再入院率，并改善整体患者流程。

## 🔬 方法详解

论文提出早期预警指数（EWI）多模态机器学习框架，整体框架整合结构化和非结构化电子健康记录（EHR）数据，通过自动特征提取预测ICU入院、紧急响应团队派遣和死亡率的综合风险。关键技术创新点包括人机协同过程，临床医生参与设定警报阈值和解释输出，以及使用SHAP（Shapley Additive exPlanations）提供可解释性，突出临床和运营风险驱动因素。与现有方法的主要区别在于其多模态数据融合能力、可解释性增强和实际部署导向，解决了传统方法数据格式不一致和缺乏临床整合的问题。

## 📊 实验亮点

最重要的实验结果：在大型医院18,633名患者数据集上，EWI实现C统计量0.796，表明高预测准确性；性能提升体现在自动风险分层和可解释输出，帮助临床医生主动管理患者，减少下游并发症。

## 🎯 应用场景

该研究应用于医院临床管理，作为患者病情恶化的早期预警工具，潜在应用包括ICU入院预测、紧急响应优化和资源分配调整，实际价值在于提升患者护理质量、减少并发症和改善医院运营效率。

## 📄 摘要（原文）

> Hospitals lack automated systems to harness the growing volume of heterogeneous clinical and operational data to effectively forecast critical events. Early identification of patients at risk for deterioration is essential not only for patient care quality monitoring but also for physician care management. However, translating varied data streams into accurate and interpretable risk assessments poses significant challenges due to inconsistent data formats. We develop a multimodal machine learning framework, the Early Warning Index (EWI), to predict the aggregate risk of ICU admission, emergency response team dispatch, and mortality. Key to EWI's design is a human-in-the-loop process: clinicians help determine alert thresholds and interpret model outputs, which are enhanced by explainable outputs using Shapley Additive exPlanations (SHAP) to highlight clinical and operational factors (e.g., scheduled surgeries, ward census) driving each patient's risk. We deploy EWI in a hospital dashboard that stratifies patients into three risk tiers. Using a dataset of 18,633 unique patients at a large U.S. hospital, our approach automatically extracts features from both structured and unstructured electronic health record (EHR) data and achieves C-statistics of 0.796. It is currently used as a triage tool for proactively managing at-risk patients. The proposed approach saves physicians valuable time by automatically sorting patients of varying risk levels, allowing them to concentrate on patient care rather than sifting through complex EHR data. By further pinpointing specific risk drivers, the proposed model provides data-informed adjustments to caregiver scheduling and allocation of critical resources. As a result, clinicians and administrators can avert downstream complications, including costly procedures or high readmission rates and improve overall patient flow.

