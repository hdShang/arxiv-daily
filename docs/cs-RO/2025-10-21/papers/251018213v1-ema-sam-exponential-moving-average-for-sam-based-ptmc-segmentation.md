---
layout: default
title: EMA-SAM: Exponential Moving-average for SAM-based PTMC Segmentation
---

# EMA-SAM: Exponential Moving-average for SAM-based PTMC Segmentation

**arXiv**: [2510.18213v1](https://arxiv.org/abs/2510.18213) | [PDF](https://arxiv.org/pdf/2510.18213.pdf)

**作者**: Maryam Dialameh, Hossein Rajabzadeh, Jung Suk Sim, Hyock Ju Kwon

---

## 💡 一句话要点

**提出EMA-SAM以解决超声视频中肿瘤分割的稳定性问题**

**关键词**: `超声视频分割` `指数移动平均` `肿瘤跟踪` `实时处理` `SAM-2扩展`

## 📋 核心要点

1. 核心问题：超声视频中低对比度、运动伪影导致SAM-2分割不稳定和漂移
2. 方法要点：引入置信度加权指数移动平均指针，增强内存库的时序一致性
3. 实验或效果：在PTMC-RFA数据集上，Dice从0.82提升至0.86，假阳性减少29%

## 📄 摘要（原文）

> Papillary thyroid microcarcinoma (PTMC) is increasingly managed with
> radio-frequency ablation (RFA), yet accurate lesion segmentation in ultrasound
> videos remains difficult due to low contrast, probe-induced motion, and
> heat-related artifacts. The recent Segment Anything Model 2 (SAM-2) generalizes
> well to static images, but its frame-independent design yields unstable
> predictions and temporal drift in interventional ultrasound. We introduce
> \textbf{EMA-SAM}, a lightweight extension of SAM-2 that incorporates a
> confidence-weighted exponential moving average pointer into the memory bank,
> providing a stable latent prototype of the tumour across frames. This design
> preserves temporal coherence through probe pressure and bubble occlusion while
> rapidly adapting once clear evidence reappears. On our curated PTMC-RFA dataset
> (124 minutes, 13 patients), EMA-SAM improves \emph{maxDice} from 0.82 (SAM-2)
> to 0.86 and \emph{maxIoU} from 0.72 to 0.76, while reducing false positives by
> 29\%. On external benchmarks, including VTUS and colonoscopy video polyp
> datasets, EMA-SAM achieves consistent gains of 2--5 Dice points over SAM-2.
> Importantly, the EMA pointer adds \textless0.1\% FLOPs, preserving real-time
> throughput of $\sim$30\,FPS on a single A100 GPU. These results establish
> EMA-SAM as a robust and efficient framework for stable tumour tracking,
> bridging the gap between foundation models and the stringent demands of
> interventional ultrasound. Codes are available here \hyperref[code
> {https://github.com/mdialameh/EMA-SAM}.

