---
layout: default
title: In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data
---

# In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data

**arXiv**: [2511.15704v1](https://arxiv.org/abs/2511.15704) | [PDF](https://arxiv.org/pdf/2511.15704.pdf)

**作者**: Xiongyi Cai, Ri-Zhao Qiu, Geng Chen, Lai Wei, Isabella Liu, Tianshu Huang, Xuxin Cheng, Xiaolong Wang

---

## 💡 一句话要点

**提出In-N-On方法，利用野外和任务数据扩展自我中心操作策略学习**

**关键词**: `自我中心视频` `操作策略学习` `数据分类` `流匹配` `领域适应` `语言条件策略`

## 📋 核心要点

1. 核心问题：自我中心视频数据异构性高，现有方法未充分利用其潜力。
2. 方法要点：分类数据为野外和任务型，构建PHSD数据集并训练语言条件流匹配策略。
3. 实验效果：Human0策略实现语言指令跟随、少样本学习和鲁棒性提升。

## 📄 摘要（原文）

> Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

