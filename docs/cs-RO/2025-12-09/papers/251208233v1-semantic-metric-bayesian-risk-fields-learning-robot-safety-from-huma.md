---
layout: default
title: Semantic-Metric Bayesian Risk Fields: Learning Robot Safety from Human Videos with a VLM Prior
---

# Semantic-Metric Bayesian Risk Fields: Learning Robot Safety from Human Videos with a VLM Prior

**arXiv**: [2512.08233v1](https://arxiv.org/abs/2512.08233) | [PDF](https://arxiv.org/pdf/2512.08233.pdf)

**作者**: Timothy Chen, Marcus Dominguez-Kuhne, Aiden Swann, Xu Liu, Mac Schwager

---

## 💡 一句话要点

**提出语义度量贝叶斯风险场框架，从人类视频中学习机器人安全风险**

**关键词**: `机器人安全` `贝叶斯风险建模` `视觉语言模型` `像素级风险估计` `轨迹优化` `人类视频学习`

## 📋 核心要点

1. 核心问题：人类安全风险是连续、上下文和空间依赖的，需从视频中提取隐式风险模型
2. 方法要点：基于贝叶斯框架，结合VLM先验和ViT似然，从RGB图像和查询对象生成像素级风险图
3. 实验或效果：模型能泛化到新对象和上下文，在机器人规划任务中产生类人运动，对齐人类偏好

## 📄 摘要（原文）

> Humans interpret safety not as a binary signal but as a continuous, context- and spatially-dependent notion of risk. While risk is subjective, humans form rational mental models that guide action selection in dynamic environments. This work proposes a framework for extracting implicit human risk models by introducing a novel, semantically-conditioned and spatially-varying parametrization of risk, supervised directly from safe human demonstration videos and VLM common sense. Notably, we define risk through a Bayesian formulation. The prior is furnished by a pretrained vision-language model. In order to encourage the risk estimate to be more human aligned, a likelihood function modulates the prior to produce a relative metric of risk. Specifically, the likelihood is a learned ViT that maps pretrained features, to pixel-aligned risk values. Our pipeline ingests RGB images and a query object string, producing pixel-dense risk images. These images that can then be used as value-predictors in robot planning tasks or be projected into 3D for use in conventional trajectory optimization to produce human-like motion. This learned mapping enables generalization to novel objects and contexts, and has the potential to scale to much larger training datasets. In particular, the Bayesian framework that is introduced enables fast adaptation of our model to additional observations or common sense rules. We demonstrate that our proposed framework produces contextual risk that aligns with human preferences. Additionally, we illustrate several downstream applications of the model; as a value learner for visuomotor planners or in conjunction with a classical trajectory optimization algorithm. Our results suggest that our framework is a significant step toward enabling autonomous systems to internalize human-like risk. Code and results can be found at https://riskbayesian.github.io/bayesian_risk/.

