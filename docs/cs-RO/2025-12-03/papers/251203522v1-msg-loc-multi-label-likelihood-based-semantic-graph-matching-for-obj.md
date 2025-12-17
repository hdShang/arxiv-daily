---
layout: default
title: MSG-Loc: Multi-Label Likelihood-based Semantic Graph Matching for Object-Level Global Localization
---

# MSG-Loc: Multi-Label Likelihood-based Semantic Graph Matching for Object-Level Global Localization

**arXiv**: [2512.03522v1](https://arxiv.org/abs/2512.03522) | [PDF](https://arxiv.org/pdf/2512.03522.pdf)

**作者**: Gihyeon Lee, Jungwoo Lee, Juwon Kim, Young-Sik Shin, Younggun Cho

---

## 💡 一句话要点

**提出基于多标签似然的语义图匹配框架，以解决未知类别和语义模糊下的机器人全局定位问题**

**关键词**: `语义图匹配` `多标签表示` `全局定位` `机器人导航` `上下文感知`

## 📋 核心要点

1. 核心问题：语义模糊加剧对象误分类和错误关联，导致机器人全局定位姿态估计误差大
2. 方法要点：利用多标签图表示捕捉对象观测的语义上下文，通过上下文感知似然传播增强图间语义对应
3. 实验或效果：在闭集和开集检测配置下评估数据关联和姿态估计性能，并在真实室内场景和合成环境中展示可扩展性

## 📄 摘要（原文）

> Robots are often required to localize in environments with unknown object classes and semantic ambiguity. However, when performing global localization using semantic objects, high semantic ambiguity intensifies object misclassification and increases the likelihood of incorrect associations, which in turn can cause significant errors in the estimated pose. Thus, in this letter, we propose a multi-label likelihood-based semantic graph matching framework for object-level global localization. The key idea is to exploit multi-label graph representations, rather than single-label alternatives, to capture and leverage the inherent semantic context of object observations. Based on these representations, our approach enhances semantic correspondence across graphs by combining the likelihood of each node with the maximum likelihood of its neighbors via context-aware likelihood propagation. For rigorous validation, data association and pose estimation performance are evaluated under both closed-set and open-set detection configurations. In addition, we demonstrate the scalability of our approach to large-vocabulary object categories in both real-world indoor scenes and synthetic environments.

