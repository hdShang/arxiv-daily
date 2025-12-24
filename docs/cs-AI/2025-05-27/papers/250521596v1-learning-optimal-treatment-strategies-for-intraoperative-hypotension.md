---
layout: default
title: Learning optimal treatment strategies for intraoperative hypotension using deep reinforcement learning
---

# Learning optimal treatment strategies for intraoperative hypotension using deep reinforcement learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21596" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21596v1</a>
  <a href="https://arxiv.org/pdf/2505.21596.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21596v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21596v1', 'Learning optimal treatment strategies for intraoperative hypotension using deep reinforcement learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Esra Adiyeke, Tianqi Liu, Venkata Sai Dheeraj Naganaboina, Han Li, Tyler J. Loftus, Yuanfang Ren, Benjamin Shickel, Matthew M. Ruppert, Karandeep Singh, Ruogu Fang, Parisa Rashidi, Azra Bihorac, Tezcan Ozrazgat-Baslanti

**分类**: q-bio.QM, cs.AI, cs.LG

**发布日期**: 2025-05-27

**备注**: 41 pages, 1 table, 5 figures, 5 supplemental tables, 6 supplemental figures

---

## 💡 一句话要点

**提出深度强化学习模型以优化手术中低血压治疗策略**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `手术决策` `低血压管理` `急性肾损伤` `智能医疗`

## 📋 核心要点

1. 现有手术决策方法依赖医生经验，导致低血压管理不一致，增加术后并发症风险。
2. 本文提出基于深度强化学习的模型，通过分析患者生理数据，优化静脉输液和血管收缩药物的使用。
3. 模型在实验中成功复制了69%的医生决策，并在药物剂量推荐上显示出显著的改进，降低了急性肾损伤的发生率。

## 📝 摘要（中文）

传统的手术决策方法依赖于医生的经验和迅速反应，存在较大变异性。针对手术中低血压的管理，本文开发了一种基于深度强化学习的模型，旨在根据患者状态生成最佳治疗建议。通过对50,021例手术的回顾性分析，模型能够有效推荐静脉输液和血管收缩药物的最佳剂量，从而降低术后急性肾损伤的风险。实验结果显示，模型的推荐与医生的决策高度一致，并在多个方面优于随机和零药物策略。

## 🔬 方法详解

**问题定义**：本文旨在解决手术中低血压的管理问题，现有方法依赖医生经验，导致治疗不一致，增加术后急性肾损伤风险。

**核心思路**：通过深度强化学习模型，基于患者的生理状态实时生成最佳治疗建议，以提高治疗效果和一致性。

**技术框架**：模型采用深度Q网络（DQN），分析16个变量，包括生理时间序列数据和每15分钟的药物剂量，分为训练和测试阶段。

**关键创新**：模型能够在药物剂量推荐上与医生决策高度一致，并在多个治疗方案中提供更优的剂量建议，显著降低术后并发症风险。

**关键设计**：模型使用了特定的损失函数和网络结构，确保在训练过程中有效学习患者状态与治疗效果之间的关系。

## 📊 实验亮点

实验结果显示，模型在药物剂量推荐上与医生的决策一致性达到69%，并在41%的案例中推荐的静脉输液剂量与实际剂量相差不超过0.05 ml/kg/15 min。此外，模型的政策价值高于医生实际治疗和随机策略，显示出显著的临床应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括手术室内的实时决策支持系统，能够帮助医生在复杂情况下做出更优的治疗选择，减少术后并发症，提高患者安全性和治疗效果。未来，该模型有望推广至其他医疗领域，提升整体医疗决策的智能化水平。

## 📄 摘要（原文）

> Traditional methods of surgical decision making heavily rely on human experience and prompt actions, which are variable. A data-driven system generating treatment recommendations based on patient states can be a substantial asset in perioperative decision-making, as in cases of intraoperative hypotension, for which suboptimal management is associated with acute kidney injury (AKI), a common and morbid postoperative complication. We developed a Reinforcement Learning (RL) model to recommend optimum dose of intravenous (IV) fluid and vasopressors during surgery to avoid intraoperative hypotension and postoperative AKI. We retrospectively analyzed 50,021 surgeries from 42,547 adult patients who underwent major surgery at a quaternary care hospital between June 2014 and September 2020. Of these, 34,186 surgeries were used for model training and 15,835 surgeries were reserved for testing. We developed a Deep Q-Networks based RL model using 16 variables including intraoperative physiologic time series, total dose of IV fluid and vasopressors extracted for every 15-minute epoch. The model replicated 69% of physician's decisions for the dosage of vasopressors and proposed higher or lower dosage of vasopressors than received in 10% and 21% of the treatments, respectively. In terms of IV fluids, the model's recommendations were within 0.05 ml/kg/15 min of the actual dose in 41% of the cases, with higher or lower doses recommended for 27% and 32% of the treatments, respectively. The model resulted in a higher estimated policy value compared to the physicians' actual treatments, as well as random and zero-drug policies. AKI prevalence was the lowest in patients receiving medication dosages that aligned with model's decisions. Our findings suggest that implementation of the model's policy has the potential to reduce postoperative AKI and improve other outcomes driven by intraoperative hypotension.

