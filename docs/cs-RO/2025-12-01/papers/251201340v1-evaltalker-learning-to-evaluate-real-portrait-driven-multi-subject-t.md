---
layout: default
title: EvalTalker: Learning to Evaluate Real-Portrait-Driven Multi-Subject Talking Humans
---

# EvalTalker: Learning to Evaluate Real-Portrait-Driven Multi-Subject Talking Humans

**arXiv**: [2512.01340v1](https://arxiv.org/abs/2512.01340) | [PDF](https://arxiv.org/pdf/2512.01340.pdf)

**作者**: Yingjie Zhou, Xilei Zhu, Siyu Ren, Ziyi Zhao, Ziwen Wang, Farong Wen, Yu Zhou, Jiezhang Cao, Xiongkuo Min, Fengjiao Chen, Xiaoyu Li, Xuezhi Cao, Guangtao Zhai, Xiaohong Liu

---

## 💡 一句话要点

**提出EvalTalker框架以评估多主体说话人视频质量，并构建首个大规模评估数据集THQA-MT。**

**关键词**: `多主体说话人生成` `视频质量评估` `多模态同步` `数据集构建` `身份一致性`

## 📋 核心要点

1. 核心问题：多主体说话人视频生成存在质量下降，缺乏评估标准。
2. 方法要点：构建THQA-MT数据集，设计EvalTalker框架感知全局质量、身份一致性和多模态同步。
3. 实验或效果：EvalTalker与主观评分相关性高，为高质量多主体说话人生成提供评估基础。

## 📄 摘要（原文）

> Speech-driven Talking Human (TH) generation, commonly known as "Talker," currently faces limitations in multi-subject driving capabilities. Extending this paradigm to "Multi-Talker," capable of animating multiple subjects simultaneously, introduces richer interactivity and stronger immersion in audiovisual communication. However, current Multi-Talkers still exhibit noticeable quality degradation caused by technical limitations, resulting in suboptimal user experiences. To address this challenge, we construct THQA-MT, the first large-scale Multi-Talker-generated Talking Human Quality Assessment dataset, consisting of 5,492 Multi-Talker-generated THs (MTHs) from 15 representative Multi-Talkers using 400 real portraits collected online. Through subjective experiments, we analyze perceptual discrepancies among different Multi-Talkers and identify 12 common types of distortion. Furthermore, we introduce EvalTalker, a novel TH quality assessment framework. This framework possesses the ability to perceive global quality, human characteristics, and identity consistency, while integrating Qwen-Sync to perceive multimodal synchrony. Experimental results demonstrate that EvalTalker achieves superior correlation with subjective scores, providing a robust foundation for future research on high-quality Multi-Talker generation and evaluation.

