---
layout: default
title: An Interpretable AI Tool for SAVR vs TAVR in Low to Intermediate Risk Patients with Severe Aortic Stenosis
---

# An Interpretable AI Tool for SAVR vs TAVR in Low to Intermediate Risk Patients with Severe Aortic Stenosis

**arXiv**: [2512.10308v1](https://arxiv.org/abs/2512.10308) | [PDF](https://arxiv.org/pdf/2512.10308.pdf)

**作者**: Vasiliki Stoumpou, Maciej Tysarowski, Talhat Azemi, Jawad Haider, Howard L. Haronian, Robert C. Hagberg, Dimitris Bertsimas

---

## 💡 一句话要点

**提出可解释的处方框架，为低至中危重度主动脉瓣狭窄患者优化SAVR与TAVR选择**

**关键词**: `可解释人工智能` `主动脉瓣狭窄治疗` `反事实建模` `最优策略树` `个体化医疗` `预后匹配`

## 📋 核心要点

1. 核心问题：临床实践中SAVR与TAVR选择因患者异质性和机构偏好而多变，缺乏可解释的个体化治疗推荐以直接优化长期结局。
2. 方法要点：集成预后匹配、反事实结果建模和最优策略树，通过反事实预测训练策略模型，将患者划分为临床一致亚组并推荐风险较低的治疗。
3. 实验或效果：在哈特福德和圣文森特医院数据上，反事实评估显示应用最优策略树处方可降低5年死亡率20.3%和13.8%，决策边界与真实世界结果和临床观察一致。

## 📄 摘要（原文）

> Background. Treatment selection for low to intermediate risk patients with severe aortic stenosis between surgical (SAVR) and transcatheter (TAVR) aortic valve replacement remains variable in clinical practice, driven by patient heterogeneity and institutional preferences. While existing models predict postprocedural risk, there is a lack of interpretable, individualized treatment recommendations that directly optimize long-term outcomes.
>   Methods. We introduce an interpretable prescriptive framework that integrates prognostic matching, counterfactual outcome modeling, and an Optimal Policy Tree (OPT) to recommend the treatment minimizing expected 5-year mortality. Using data from Hartford Hospital and St. Vincent's Hospital, we emulate randomization via prognostic matching and sample weighting and estimate counterfactual mortality under both SAVR and TAVR. The policy model, trained on these counterfactual predictions, partitions patients into clinically coherent subgroups and prescribes the treatment associated with lower estimated risk.
>   Findings. If the OPT prescriptions are applied, counterfactual evaluation showed an estimated reduction in 5-year mortality of 20.3\% in Hartford and 13.8\% in St. Vincent's relative to real-life prescriptions, showing promising generalizability to unseen data from a different institution. The learned decision boundaries aligned with real-world outcomes and clinical observations.
>   Interpretation. Our interpretable prescriptive framework is, to the best of our knowledge, the first to provide transparent, data-driven recommendations for TAVR versus SAVR that improve estimated long-term outcomes both in an internal and external cohort, while remaining clinically grounded and contributing toward a more systematic and evidence-based approach to precision medicine in structural heart disease.

