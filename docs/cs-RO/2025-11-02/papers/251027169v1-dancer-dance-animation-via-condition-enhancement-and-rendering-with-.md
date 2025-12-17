---
layout: default
title: DANCER: Dance ANimation via Condition Enhancement and Rendering with diffusion model
---

# DANCER: Dance ANimation via Condition Enhancement and Rendering with diffusion model

**arXiv**: [2510.27169v1](https://arxiv.org/abs/2510.27169) | [PDF](https://arxiv.org/pdf/2510.27169.pdf)

**作者**: Yucheng Xing, Jinxing Yin, Xiaodong Liu

---

## 💡 一句话要点

**提出DANCER框架以增强条件生成单人物舞蹈视频**

**关键词**: `舞蹈视频生成` `扩散模型` `条件增强` `姿态渲染` `数据集构建`

## 📋 核心要点

1. 核心问题：单人物舞蹈视频生成因人体运动自由度大而具挑战性。
2. 方法要点：引入外观增强模块和姿态渲染模块，优化参考图像和运动条件。
3. 实验或效果：在真实数据集上评估，性能优于现有先进方法。

## 📄 摘要（原文）

> Recently, diffusion models have shown their impressive ability in visual
> generation tasks. Besides static images, more and more research attentions have
> been drawn to the generation of realistic videos. The video generation not only
> has a higher requirement for the quality, but also brings a challenge in
> ensuring the video continuity. Among all the video generation tasks,
> human-involved contents, such as human dancing, are even more difficult to
> generate due to the high degrees of freedom associated with human motions. In
> this paper, we propose a novel framework, named as DANCER (Dance ANimation via
> Condition Enhancement and Rendering with Diffusion Model), for realistic
> single-person dance synthesis based on the most recent stable video diffusion
> model. As the video generation is generally guided by a reference image and a
> video sequence, we introduce two important modules into our framework to fully
> benefit from the two inputs. More specifically, we design an Appearance
> Enhancement Module (AEM) to focus more on the details of the reference image
> during the generation, and extend the motion guidance through a Pose Rendering
> Module (PRM) to capture pose conditions from extra domains. To further improve
> the generation capability of our model, we also collect a large amount of video
> data from Internet, and generate a novel datasetTikTok-3K to enhance the model
> training. The effectiveness of the proposed model has been evaluated through
> extensive experiments on real-world datasets, where the performance of our
> model is superior to that of the state-of-the-art methods. All the data and
> codes will be released upon acceptance.

