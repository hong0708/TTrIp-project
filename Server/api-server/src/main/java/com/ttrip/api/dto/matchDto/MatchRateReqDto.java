package com.ttrip.api.dto.matchDto;

import com.ttrip.core.entity.matchHistory.MatchHistory;
import com.ttrip.core.entity.member.Member;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.UUID;

@Data
@ApiModel(value = "MatchRateReqDto: 매칭 기록 생성", description = "매칭 기록 생성")
public class MatchRateReqDto {
    @ApiModelProperty(value = "피평가자 uuid", example = "d60791eb-da68-42b5-86a3-d6583cfa0617")
    private Integer matchHistoryId;
    @ApiModelProperty(value = "평가 점수", example = "4")
    private Integer rate;
}
