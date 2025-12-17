---
layout: default
title: Autonomous Surface Selection For Manipulator-Based UV Disinfection In Hospitals Using Foundation Models
---

# Autonomous Surface Selection For Manipulator-Based UV Disinfection In Hospitals Using Foundation Models

**arXiv**: [2511.18709v1](https://arxiv.org/abs/2511.18709) | [PDF](https://arxiv.org/pdf/2511.18709.pdf)

**作者**: Xueyan Oh, Jonathan Her, Zhixiang Ong, Brandon Koh, Yun Hann Tan, U-Xuan Tan

---

## 💡 一句话要点

**提出基于基础模型的自主表面选择方法以简化医院机械臂UV消毒**

**关键词**: `UV消毒` `基础模型` `表面分割` `机械臂控制` `视觉语言模型`

## 📋 核心要点

1. 核心问题：传统UV消毒方法依赖人工定义消毒区域，自动化困难且缺乏部分表面理解。
2. 方法要点：利用基础模型简化表面选择，无需模型训练，并引入VLM辅助分割精炼。
3. 实验或效果：分割成功率超92%，真实实验验证了实际应用潜力。

## 📄 摘要（原文）

> Ultraviolet (UV) germicidal radiation is an established non-contact method for surface disinfection in medical environments. Traditional approaches require substantial human intervention to define disinfection areas, complicating automation, while deep learning-based methods often need extensive fine-tuning and large datasets, which can be impractical for large-scale deployment. Additionally, these methods often do not address scene understanding for partial surface disinfection, which is crucial for avoiding unintended UV exposure. We propose a solution that leverages foundation models to simplify surface selection for manipulator-based UV disinfection, reducing human involvement and removing the need for model training. Additionally, we propose a VLM-assisted segmentation refinement to detect and exclude thin and small non-target objects, showing that this reduces mis-segmentation errors. Our approach achieves over 92\% success rate in correctly segmenting target and non-target surfaces, and real-world experiments with a manipulator and simulated UV light demonstrate its practical potential for real-world applications.

