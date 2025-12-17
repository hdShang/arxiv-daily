---
layout: default
title: Generative Photographic Control for Scene-Consistent Video Cinematic Editing
---

# Generative Photographic Control for Scene-Consistent Video Cinematic Editing

**arXiv**: [2511.12921v1](https://arxiv.org/abs/2511.12921) | [PDF](https://arxiv.org/pdf/2511.12921.pdf)

**作者**: Huiqiang Sun, Liao Shen, Zhan Peng, Kun Wang, Size Wu, Yuhang Zang, Tianqi Liu, Zihao Huang, Xingyu Zeng, Zhiguo Cao, Wei Li, Chen Change Loy

---

## 💡 一句话要点

**提出CineCtrl框架以实现视频电影编辑中对摄影参数的精细控制**

**关键词**: `视频生成` `摄影控制` `解耦注意力` `电影编辑` `数据集构建`

## 📋 核心要点

1. 核心问题：现有生成视频模型难以控制摄影元素如景深和曝光，仅限相机运动控制
2. 方法要点：引入解耦交叉注意力机制，分离相机运动与摄影输入，实现独立精细控制
3. 实验或效果：通过大规模数据集训练，生成高保真视频，精确控制用户指定摄影效果

## 📄 摘要（原文）

> Cinematic storytelling is profoundly shaped by the artful manipulation of photographic elements such as depth of field and exposure. These effects are crucial in conveying mood and creating aesthetic appeal. However, controlling these effects in generative video models remains highly challenging, as most existing methods are restricted to camera motion control. In this paper, we propose CineCtrl, the first video cinematic editing framework that provides fine control over professional camera parameters (e.g., bokeh, shutter speed). We introduce a decoupled cross-attention mechanism to disentangle camera motion from photographic inputs, allowing fine-grained, independent control without compromising scene consistency. To overcome the shortage of training data, we develop a comprehensive data generation strategy that leverages simulated photographic effects with a dedicated real-world collection pipeline, enabling the construction of a large-scale dataset for robust model training. Extensive experiments demonstrate that our model generates high-fidelity videos with precisely controlled, user-specified photographic camera effects.

